"""
The Python standard library's 'calendar' module allows you to 
render a calendar to your terminal.
https://docs.python.org/3.6/library/calendar.html

Write a program that accepts user input of the form
  `calendar.py month [year]`
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
#adjusted this so that you can enter only the year by
#typing andything then a year (followed by a space) it
#will print curmonth useryear.
#This is more user friendly and was much harder to do.
#It also handles 3 letter abrivation and full name months
#years auto convert from 10-99 to 2010-2099 and 0010-0099
#how you call dates in this range.
#also made this a loop so it will keep repeating till the
#user types 'q' which it is only told after the first cycle.

import sys
import calendar
from datetime import datetime

date = datetime.date(datetime.today());
cal = calendar.TextCalendar();

def handle_month(m):
    try:
        int(m);
        if(int(m) < 1 or int(m) > 12):
            raise;
    except:
        try:
            m = stringmonths[m];
        except:
            m = -1;
    return m;

def handle_year(y):
    try:
        if(int(y) > 9999 or int(y) < 1):
            raise;
        if(len(y) == 2):
            y = "20" + y;
    except:
        y =  -1;
    return y;
            
while (True):
    stringmonths = { "jan":1, "january":1, "feb":2, "february":2, "mar":3, "march":3, "apr":4, "april":4, "may":5, "jun":6, "june":6, "jul":7, "july":7, "aug":8, "august":8, "sep":9, "september":9, "oct":10, "october":10, "nov":11, "november":11, "dec":12, "december":12 }

    userinput = input("Please Enter a Month and/or Year: ").lower().split(" ");
    if(userinput[0] == "q"):
        break;
    date = datetime.date(datetime.today());
    cal = calendar.TextCalendar();
    if len(userinput) > 0:
        userinput[0] = handle_month(userinput[0]);
    else:
        userinput.append(-1);
    if len(userinput) > 1:
        userinput[1] = handle_year(userinput[1])
    else:
        userinput.append(-1);
    
    if(userinput[0] == -1 or userinput[1] == -1):
        if(userinput[0] == -1 and userinput[1] == -1):
            print("\n\nPlease enter month followed by year. \nValid Month sytax: (1-12 or Jan - Dec or January - December)\nVaild Year format (1-9999 years 10-99 become 2010-2099 use 0010-0099 for dates in that range).\nIf you wish to get the current month of a given year type '*' then year.\n\n");
            continue;
        if(userinput[0] == -1):
            userinput[0] = date.month;
        if(userinput[1] == -1):
            userinput[1] = date.year;

    print("\n\n"+cal.formatmonth(int(userinput[1]), int(userinput[0])));
    print("\nType \'q\' to quit");
