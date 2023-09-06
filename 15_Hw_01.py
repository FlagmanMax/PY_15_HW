# Возьмите любые 1-3 задания из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.


# Напишите следующие функции:
# ○ Нахождение корней квадратного уравнения
# ○ Декоратор, запускающий функцию нахождения корней квадратного


from random import randint
import argparse
import locale
locale.setlocale(locale.LC_ALL, "Russian")

import logging
logging.basicConfig(
    level=logging.INFO,
    filename='15_Hw_01.log',
    filemode='a',
    style='{',
    encoding='utf-8',
    format='{name}: {asctime} {levelname} {funcName} {lineno} -> {msg}')

def deco_abc(func):
    '''
    Decorator function
    :param func:
    :return:
    '''
    def inner(abc):
        result = {}
        roots = func(abc)
        a, b, c = abc
        result[f'{a=}, {b=}, {c=}'] = roots
        return result
    return inner

def get_non_zero_rand():
    """
    Generate random not zero value
    :return:
    """
    x = 0
    while x==0:
        x = randint(-100, 100)
    return x

def generate_coeffs() -> tuple[int, int, int]:
    """
    generate tuple with 3 coeffs, the first is non zero value
    :return:
    """
    return [get_non_zero_rand(),randint(-100,100),randint(-100,100)]

@deco_abc
def quadratic_equation(abc: tuple[int, int, int]) -> tuple:
    """
    Qiadratic equation solver
    :param abc:
    :return:
    """
    a, b, c = abc
    logging.info(f'a = {a}, b= {b}, c = {c}')
    d = b ** 2 - 4 * a * c
    if d > 0:
        x1 = round((-b + d ** 0.5) / (2 * a) , 2)
        x2 = round((-b - d ** 0.5) / (2 * a) , 2)
        logging.info(f'2 roots found: {x1}, {x2}')
        return x1, x2
    elif d == 0:
        logging.info(f'1 root found: {x1}')
        x1 = round(-b/(2*a),2)
        return (x1,)
    else:
        logging.error(f'No roots found')
        return (None,)


if __name__ == '__main__':
    coeffs = generate_coeffs()

    parser = argparse.ArgumentParser(description='Quadratic equation solver')
    parser.add_argument('-a', type=float, help = 'Coefficient a', default = coeffs[0])
    parser.add_argument('-b', type=float, help = 'Coefficient b', default = coeffs[1])
    parser.add_argument('-c', type=float, help = 'Coefficient c', default = coeffs[2])
    args = parser.parse_args()

    result = quadratic_equation((args.a, args.b, args.c))
    print(result)
