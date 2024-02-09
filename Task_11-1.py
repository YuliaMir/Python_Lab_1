'''Каждый третий четверг каждого месяца билеты в Эрмитаж
бесплатны. Напечатайте список дат в 2023 году, когда вход бесплатен.'''


import calendar

def no_payment_dates(year):
    free_dates = []
    for month in range(1, 13):
        cal = calendar.monthcalendar(year, month)
        third_thursdays = [week[3] for week in cal if week[3] != 0]
        if len(third_thursdays) >= 3:
            free_date = third_thursdays[2]
            free_dates.append(f"{year}-{month:02d}-{free_date:02d}")
    return free_dates

year = 2023
free_dates = no_payment_dates(year)
for date in free_dates:
    print(date)
