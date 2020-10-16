from datetime import datetime, timedelta

dt = datetime(2020, 10, 16, 11, 22, 50)
add_dt = dt + timedelta(days = 5)
print(dt.year)
print(dt.month)
print(dt.day)
print(dt.hour)
print(dt.minute)
print(dt.second)
print(add_dt)