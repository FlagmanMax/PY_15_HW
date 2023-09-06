# Задание №3
# Доработаем задачу 2.
# Сохраняйте в лог файл раздельно:
# ○ уровень логирования,
# ○ дату события,
# ○ имя функции (не декоратора),
# ○ аргументы вызова,
# ○ результат.

import logging
logging.basicConfig(
    level=logging.INFO,
    filename='15_Task_03.log',
    filemode='w',
    style = '{',
    encoding = 'utf-8',
    format='{name}: {asctime} {levelname} {funcName} {lineno} -> {msg}')

def log_deco(func):
    def wrapper(x, y):
        try:
            logging.info(f'Func {func.__name__} Args: {x} {y}; Res = {func(x, y)}')
        except:
            logging.ERROR('Some error')
    return wrapper

@log_deco
def log_div(x, y):
    return(x/y)

@log_deco
def log_mult(x, y):
    return(x*y)

x, y = map(int, input('Введите 2 целых числа через пробел ').split())
log_div(x, y)
log_mult(x, y)