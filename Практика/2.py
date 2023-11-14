import calendar

weekdays = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']

day, month, year = map(int, input().split())
print(weekdays[calendar.weekday(year, month, day)])
print(*weekdays)