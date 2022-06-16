#!/usr/bin/env python3

import math

n = int(input())

if n == 0:
    print("Yes")
elif n < 0 and 0 <= math.log2(abs(n)) <= 31:
    print("Yes")
elif n >= 0 and 0 <= math.log2(abs(n)) < 31:
    print("Yes")
else:
    print("No")
