from datetime import datetime, timedelta

def is_lucky_date(date):
    day_number = date.day
    day_of_week = date.strftime("%A")
    if day_number % 4 != 0 and day_of_week != "Monday":
        return True
    return False

def find_lucky_dates(start_date, n):
    lucky_dates = []
    current_date = start_date
    while len(lucky_dates) < 3:
        if is_lucky_date(current_date):
            lucky_dates.append(current_date)
        current_date += timedelta(days=n)
    return lucky_dates

input_date = input("Введите исходную дату в формате YYYY/MM/DD: ")
n = int(input("Введите число n: "))

start_date = datetime.strptime(input_date, "%Y/%m/%d")
lucky_dates = find_lucky_dates(start_date, n)

for date in lucky_dates:
    formatted_date = date.strftime("%d %B, %A")
    print(formatted_date)
