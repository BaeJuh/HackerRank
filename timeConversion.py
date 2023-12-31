#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    hour, minute, second = s[:-2].split(":")

    if (s[-2:] == "PM"):
        if (hour == "12"):
            hour = "12"
        else:
            hour = str(int(hour) + 12)
    if (s[-2:] == "AM" and hour == "12"):
        hour = "00"

    return hour + ":" + minute + ":" + second


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
