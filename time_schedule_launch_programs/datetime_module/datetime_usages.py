import datetime, time

dt = datetime.datetime.fromtimestamp(1_000_000)
print(dt)

dt_now = datetime.datetime.fromtimestamp(time.time())
print(dt_now)

# comparing datetimes

halloween_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)
new_year_2027 = datetime.datetime(2027, 1, 1, 0, 0, 0)
oct_31_2026 = datetime.datetime(2026, 10, 31, 0, 0, 0)

print(halloween_2026 == new_year_2027)
print(halloween_2026 == oct_31_2026)
print(halloween_2026 != oct_31_2026)
