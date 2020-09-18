from datetime import date, timedelta, datetime
print(f'Сегодня {date.today()}')
print(f'Вчера было {date.today()+timedelta(days=-1)}')
print(f'30 дней назад было {date.today()+timedelta(days=-30)}')
date_string = '01/01/25 12:10:03.234567'
print(f'Дата из строки {datetime.strptime(date_string, "%d/%m/%y %H:%M:%S.%f")}')

