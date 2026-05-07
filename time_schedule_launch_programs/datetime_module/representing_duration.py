import datetime

delta = datetime.timedelta(days=11, hours=10, minutes=9, seconds=8)

print(delta.days, delta.seconds, delta.microseconds)
print(delta.total_seconds())
print(delta)

# calculate date arithmetics
now = datetime.datetime.now()
thousand_days = datetime.timedelta(1000)

print(now + thousand_days)

oct_21st = datetime.datetime(2026, 10, 21, 16, 29, 0)
about_thirty_years = datetime.timedelta(days=365 * 30)
print(oct_21st - about_thirty_years)
