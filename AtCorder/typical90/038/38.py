#!/usr/bin/env python3

from math import gcd

a, b = map(int, input().split())

lcm = a * b // gcd(a, b)

if lcm <= 10**18:
    print(lcm)
else:
    print("Large")
