"""
The Python standard library's 'calendar' module allows you to
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `14_cal.py month [year]`
and does the following:
 - If the user doesn't specify any input, your program should
   print the calendar for the current month. The 'datetime'
   module may be helpful for this.
 - If the user specifies one argument, assume they passed in a
   month and render the calendar for that month of the current year.
 - If the user specifies two arguments, assume they passed in
   both the month and the year. Render the calendar for that
   month and year.
 - Otherwise, print a usage statement to the terminal indicating
   the format that your program expects arguments to be given.
   Then exit the program.
"""

import sys
import calendar
from datetime import datetime

argLength = len(sys.argv)

now = datetime.now()


def printCalendar(month=now.month, year=now.year):
    print(calendar.month(year, month))


argError = 'The first argument must be a month in number form, from 1 to 12. The second argument (if entered) must be a year in number form'

try:
    if argLength == 1:
        printCalendar()
    elif argLength == 2:
        if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 12:
            printCalendar(int(sys.argv[1]))
        else:
            print(argError)
    else:
        if int(sys.argv[1]) >= 1 and int(sys.argv[1]) <= 12:
            printCalendar(int(sys.argv[1]), int(sys.argv[2]))
except ValueError:
    print(argError)
