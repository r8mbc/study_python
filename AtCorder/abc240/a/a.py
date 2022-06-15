#!/usr/bin/env python3

a, b = map(int, input().split())

if abs(a - b) == 1:
    print("Yes")
elif abs(a - b) == 9:
    print("Yes")
else:
    print("No")
