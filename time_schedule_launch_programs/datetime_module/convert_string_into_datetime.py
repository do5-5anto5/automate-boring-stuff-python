import datetime

str_time = datetime.datetime.strptime('October 21, 2026', '%B %d, %Y')
print(str_time)

str_time = datetime.datetime.strptime('2026/10/21 16:29:00', '%Y/%m/%d %H:%M:%S')
print(str_time)

str_time = datetime.datetime.strptime("November of '63", "%B of '%y")
print(str_time)

str_time = datetime.datetime.strptime("November of '73", "%B of '%y")
print(str_time)
