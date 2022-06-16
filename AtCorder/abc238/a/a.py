#!/usr/bin/env python3

import math

n = int(input())


if n * math.log(2) > 2 * math.log(n):
    print("Yes")
else:
    print("No")
