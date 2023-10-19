#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    # Write your code here
    arr_copy = []
    max = 0
    min = sum(arr)

    for i in arr:
        arr_copy = arr

        sum_arr = sum(arr_copy) - i

        if (sum_arr > max):
            max = sum_arr
        elif (sum_arr < min):
            min = sum_arr

    print(min, max)

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
