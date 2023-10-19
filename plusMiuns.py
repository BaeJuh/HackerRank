#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(n, arr):
    pos = 0
    neg = 0
    zero = 0

    for i in range(n):
        if arr[i] == 0:
            zero += 1
        elif arr[i] > 0:
            pos += 1
        elif arr[i] < 0:
            neg += 1

    print(format(pos/n, ".6f"))
    print(format(neg/n, ".6f"))
    print(format(zero/n, ".6f"))

if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(n, arr)
