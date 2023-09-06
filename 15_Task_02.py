# Задание №2
# На семинаре про декораторы был создан логирующий
# декоратор. Он сохранял аргументы функции и результат её
# работы в файл.
# Напишите аналогичный декоратор, но внутри используйте
# модуль logging.
import logging
logging.basicConfig(
    level=logging.INFO,
    filename='15_Task_02.log',
    filemode='w',
    format='%(asctime)s, %(levelname)s, %(message)s')

def log_deco(func):
    def wrapper(x, y):
        try:
            logging.info(f'{x}/{y} = {func(x, y)}')
        except:
            logging.ERROR('Some error')
    return wrapper

@log_deco
def log_div(x, y):
    return(x/y)

x, y = map(int, input('Введите 2 целых числа через пробел ').split())
log_div(x, y)