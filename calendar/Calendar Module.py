import calendar
date = input().split()
month,day,year = list(map(int,date))
days = ['monday','tuesday','wednesday','thursday','friday','saturday','sunday']
number = calendar.weekday(year,month,day)
print(days[number].upper())