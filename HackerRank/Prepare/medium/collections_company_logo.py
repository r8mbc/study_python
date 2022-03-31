# https://www.hackerrank.com/challenges/most-commons/problem?isFullScreen=true

#!/bin/python3

import math
import os
import random
import re
import sys
import collections


if __name__ == "__main__":
    s = input()
    s = collections.Counter(s)
    s = sorted(s.items(), key=lambda x: x[0])
    s = sorted(s, key=lambda x: x[1], reverse=True)

    for k, v in s[:3]:
        print(k, v)
