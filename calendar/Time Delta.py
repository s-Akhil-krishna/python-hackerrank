#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime
def time_delta(t1, t2):
    f = "%a %d %b %Y %H:%M:%S %z"
    d1 = datetime.strptime(t1,f)
    d2 = datetime.strptime(t2,f)
    diff = (d1-d2).total_seconds()
    return str(abs(int(diff)))

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + '\n')

    fptr.close()
