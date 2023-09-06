# Задание №4
# Функция получает на вход текст вида: “1-й четверг ноября”, “3-
# я среда мая” и т.п.
# Преобразуйте его в дату в текущем году.
# Логируйте ошибки, если текст не соответсвует формату.

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

def parse_date():
    date_string = input('Введите дату:')
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
            break
        weekday_count += 1
        some_date += timedelta(days = 1)

    return some_date

try:
    print(parse_date())
except Exception as e:
    logging.basicConfig(level=logging.INFO,
                        filename="15_Task_04.log",
                        filemode="a",
                        format='%(levelname)s, %(asctime)s, %(message)s')
    logging.error(f"Wrong date!: {e}")

