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
    The valid_date() function will take a date in "YYYY-MM-DD" format, and return in appropriate format in order of year, month, day.
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
    The leap_year() function will take a year in "YYYY" format, and return True if it is leap year or False otherwise.  
    """
    leapyear = year % 4

    if leapyear == 0:

       return True

    else:

       return False


