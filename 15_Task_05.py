# Задание №5
# Дорабатываем задачу 4.
# Добавьте возможность запуска из командной строки.
# При этом значение любого параметра можно опустить. В
# этом случае берётся первый в месяце день недели, текущий
# день недели и/или текущий месяц.
# *Научите функцию распознавать не только текстовое
# названия дня недели и месяца, но и числовые,
# т.е не мая, а 5.
import argparse
import locale
locale.setlocale(locale.LC_ALL, "Russian")
from datetime import date, timedelta
import logging

weekdays = {
    'понедельник': 0,
    'вторник': 1,
    'среда': 2,
    'четверг': 3,
    'пятница': 4,
    'суббота': 5,
    'воскресенье': 6
}

months = {
    'января': 1,
    'февраля': 2,
    'марта': 3,
    'апреля': 4,
    'мая': 5,
    'июня': 6,
    'июля': 7,
    'августа': 8,
    'сентября': 9,
    'октября': 10,
    'ноября': 11,
    'декабря': 12
}

def parse_date(date_string):
    # date_string = input('Введите дату:')
    date_words = []
    date_words = date_string.split()
    day_num,_ = date_words[0].split('-')
    day_num = int(day_num)
    week_day = date_words[1]
    month = date_words[2]
    print(f'{day_num=}, {week_day=}, {month=}')

    some_date = date(2023, months[month], 1)
    weekday_count = 0
    while weekday_count < 7:
        # print(f'{some_date.weekday()=} {weekdays[week_day]}')
        if some_date.weekday() == weekdays[week_day]:
            some_date += timedelta(days=((day_num-1) * 7))
            logging.info(f"Date = {some_date}, String = {date_string}")
            break
        weekday_count += 1
        some_date += timedelta(days = 1)

    return some_date

# str_input = '4-ый четверг ноября'
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Date logger')
    parser.add_argument('-a', type=str, help='Введите день недели и месяца', default = '1-ый')
    parser.add_argument('-b', type=str, help='Текущий день недели', default = 'вторник')
    parser.add_argument('-c', type=str, help='Текущий месяц', default = 'сентября')
    args = parser.parse_args()
    print(args.a)
    print(args.b)
    print(args.c)
    args_string = args.a +' ' + args.b + ' '+ args.c
    print(args_string)
    logging.basicConfig(level=logging.INFO,
                        filename="15_Task_05.log",
                        filemode="a",
                        format='%(levelname)s, %(asctime)s, %(message)s',
                        encoding = 'utf-8'
                        )

    try:
        print(parse_date(args_string))
    except Exception as e:
        logging.error(f"Wrong date!: {e}")