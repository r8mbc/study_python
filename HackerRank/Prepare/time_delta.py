# https://www.hackerrank.com/challenges/python-time-delta/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

#!/bin/python3

import math
import os
import random
import re
import sys

from datetime import datetime

# Complete the time_delta function below.


def time_delta(t1, t2):
    format = "%a %d %b %Y %H:%M:%S %z"
    a = int(
        (
            abs(datetime.strptime(t1, format) - datetime.strptime(t2, format))
        ).total_seconds()
    )
    return str(a)


if __name__ == "__main__":
    fptr = open(os.environ["OUTPUT_PATH"], "w")

    t = int(input())

    for t_itr in range(t):
        t1 = input()

        t2 = input()

        delta = time_delta(t1, t2)

        fptr.write(delta + "\n")

    fptr.close()
