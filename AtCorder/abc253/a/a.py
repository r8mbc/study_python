#!/usr/bin/env python3

a, b, c = map(int, input().split())

if a >= b >= c or c >= b >= a:
    print("Yes")
else:
    print("No")
