from datetime import datetime, timedelta

mydate = datetime(2020, 10, 16, 11, 58, 12)
x = 0
while x <10:
    print(mydate)

    mydate = mydate + timedelta(days=14)
    x = x + 1




