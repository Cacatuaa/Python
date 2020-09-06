import calendar

month, day, year = map(int, input("").split())
day = calendar.weekday(year, month, day)
print(calendar.day_name[day].upper())