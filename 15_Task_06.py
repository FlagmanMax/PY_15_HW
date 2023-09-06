# Задание №6
# Напишите код, который запускается из командной строки и получает на вход
# путь до директории на ПК.
# Соберите информацию о содержимом в виде объектов namedtuple.
# Каждый объект хранит:
# ○ имя файла без расширения или название каталога,
# ○ расширение, если это файл,
# ○ флаг каталога,
# ○ название родительского каталога.
# В процессе сбора сохраните данные в текстовый файл используя
# логирование.

from collections import namedtuple
import os
import argparse
import locale
locale.setlocale(locale.LC_ALL, "Russian")
from datetime import date, timedelta
import logging

def file_smth(path = '.'):
    """
    Recursively check this folder
    :param path: path to the folder
    :return:
    """
    for dirpath, dir_name, file_name in os.walk(path):
        Files = namedtuple('Files', ['item_name', 'file_ext', 'dir_flag', 'parent_dir'])
        parent_path = dirpath.split('\\')[-2]

        if dir_name:
            dir_flag = 'Is a directory'
            exp_dict = Files(dir_name, None, dir_flag, parent_path)
            logging.info(f'{exp_dict}')

        if file_name:
            dir_flag = 'Is a file'
            for f in file_name:
                exp_dict = Files(f.split('.')[0], f.split('.')[-1], dir_flag, parent_path)
                logging.info(f'{exp_dict}')

    save_in_file(exp_dict)

def save_in_file(some_path):
    logging.basicConfig(level=logging.INFO,
                        filename="15_Task_06.log",
                        filemode="a",
                        format='%(levelname)s, %(asctime)s, %(message)s',
                        encoding='utf-8'
                        )
    file_smth(some_path)

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Directory parser')
    parser.add_argument('-path', type=str, help = 'Path to directory', default = os.getcwd())
    args = parser.parse_args()

    save_in_file(args.path)