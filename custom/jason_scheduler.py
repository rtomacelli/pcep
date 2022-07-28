# Create a function in Python that accepts two parameters. They’ll both be numbers. The first will be the month as a 
# number, and the second will be the four-digit year. The function should parse the parameters and return True if the 
# month contains a Friday the 13th and False if it doesn’t.

import calendar
import datetime

def jason_scheduler(month, year):
    days_of_month = calendar.monthrange(year,month)[1]
    for day in range(1, days_of_month):
        today = datetime.datetime(year, month, day)
        if(today.weekday() == 4 and day == 13):
            print("Today is friday!" , day , "/" , month , "kill'em all!")
        else:
            print("Today is " , day , "/" , month , " go back to bed Jason! there's no room for you!")


jason_scheduler(5, 2023)
