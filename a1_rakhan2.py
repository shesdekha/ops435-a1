#!/usr/bin/env python3

"""
OPS435 Assignment 1 - Winter 2020
Program: a1_rakhan2.py
Author: Rajib Khan
The python code in this file (a1_rakhan2.py) is original work written by
Rajib Khan. No code in this file is copied from any other source
except those provided by the course instructor, including any person,
textbook, or on-line resource. I have not shared this python script
with anyone or anything except for submission for grading.  
I understand that the Academic Honesty Policy will be enforced and
violators will be reported and appropriate action will be taken.
"""

import sys
import os

def usage():

    """
    The usage() function will take an arguments to use the script and exit
    """

    if len(sys.argv) != 3 and len(sys.argv) != 4:
        print('Usage: ' + sys.argv[0] + ' [--step]' + ' YYYYMMDD' + ' -/+')
        sys.exit()

def valid_date(today):

    """
    The valid_date() function will take a date in "YYYY-MM-DD" format, and return in appropriate form    at in order of year, month, day.
    """
    if len(today) != 10:
       return('Error: wrong date entered')
       sys.exit()

    else:
        str_y, str_m, str_d = today.split('-')
        year = int(str_y)
        month = int(str_m)
        day = int(str_d)
        if month > 12 or month < 1:
           sys.exit('Error: wrong month entered')
        else:
           mon_max = days_in_mon(year)
           to_day = mon_max[month]
           if day > to_day:
                 sys.exit('Error: wrong day entered')

           else:
                 return True


def leap_year(year):
    """
    The leap_year() function will take a year in "YYYY" format, and return True if it is leap year or    False otherwise.  
    """
    lyear = year % 4

    if lyear == 0:

       return True

    else:

       return False

def days_in_mon(year):

    """
    The days_in_mon() function will take a year in "YYYY" format, and return a the number of days in     a month of a year.
    """

    not_lyear = leap_year(year)

    if not_lyear is False:

       feb_max = 28

    else:

       feb_max = 29

    mon_max = { 1:31, 2:feb_max, 3:31, 4:30, 5:31, 6:30, 7:31, 8:31, 9:30, 10:31, 11:30, 12:31}

    return mon_max

def after(today):

    """
    after(today) -> str
        after() takes a valid date string in 'YYYY-MM-DD' format and return a
        date string for the next day in 'YYYY-MM-DD' format.
        e.g. after('2017-12-31') -> '2018-01-01'
             after('2018-01-31') -> '2018-02-01'
             after('2018-02-28') -> '2018-03-01'
    """

    valid_date(today)

    if valid_date(today) != True:

        return('Error: wrong date entered')
        sys.exit()

    else:

        str_y, str_m, str_d = today.split('-')

        year = int(str_y)

        month = int(str_m)

        day = int(str_d)

        tmp_day = day + 1

        mon_max = days_in_mon(year)

        if tmp_day > mon_max[month]:

           to_day = tmp_day % mon_max[month] 
           
           tmp_month = month + 1

        else:

           to_day = tmp_day

           tmp_month = month + 0

        if tmp_month > 12:

           to_month = 1

           year = year + 1

        else:
    
            to_month = tmp_month + 0

        next_date = str(year)+"-"+str(to_month).zfill(2)+"-"+str(to_day).zfill(2)

        return next_date

def before(today):

     """
     before(today) -> str
        before() takes a valid date string in 'YYYY-MM-DD' format and return a
        date string for the previous day in 'YYYY-MM-DD' format.
        e.g. after('2017-12-31') -> '2017-12-30'
             after('2018-01-31') -> '2018-01-30'
             after('2018-02-28') -> '2018-02-27'
     """

     valid_date(today)


     if valid_date(today) != True:
        print(usage())

     else:
         str_y, str_m, str_d = today.split('-')
         year = int(str_y)
         month = int(str_m)
         day = int(str_d)
         tmp_day = day - 1 
         mon_max = days_in_mon(year)

     if tmp_day == 0:
        tmp_month = month - 1
        if tmp_month == 0:
           month=12
           tmp_month = 12
           to_day= mon_max[tmp_month]
           year = year - 1

        else:
            month=tmp_month - 0

            to_day = mon_max[tmp_month]

     else:

           to_day = tmp_day
           tmp_month = month - 0

     next_date = str(year)+"-"+str(month).zfill(2)+"-"+str(to_day).zfill(2)

     return next_date


def dbda(today,days,step):

    """
    The dbda() function is the main function of this script.  The dbda() function will take a date in    "YYYY-MM-DD" format, takes a postive or negative interger and return the value according to requi    red increase or decrease integer format.  
    """

    if int(days) >= 0:

           count = 0

           while count != int(days):

                 today = after(today)

                 count = count + 1

                 if step == 1 and count != int(days):

                           print(today)

           return today

    else:

           count = 0

           while count != int(days):

                today = before(today)

                count = count - 1

                if step == 1 and count != int(days):

                         print(today)

           return today

if __name__ == '__main__':
    if len(sys.argv) == 3:
        if len(sys.argv[2]) == 10:          
            print(dbda(sys.argv[1],sys.argv[2]))
        else:
            print(dbda(sys.argv[1],sys.argv[2],0))
    elif len(sys.argv) == 4:
        print(dbda(sys.argv[2],sys.argv[3],1))
    else:
        print('Usage: ' + sys.argv [0] + ' [--step]' + ' YYYY-MM-DD +/-n')
