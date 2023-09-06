# Задание №1
# Напишите программу, которая использует модуль logging для
# вывода сообщения об ошибке в файл.
# Например отлавливаем ошибку деления на ноль.

import logging
logging.basicConfig(
    level=logging.INFO,
    filename='15_Task_01.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s')

# logger = logging.getLogger(__name__)

x, y = map(int, input('Введите 2 целых числа через пробел ').split())

try:
    print(x/y)
except:
    logging.error('ZeroDivisionError')
