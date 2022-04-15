#!/usr/bin/env python3

a, b, c, x = map(int, input().split())


if x <= a:
    print(f"1.000000000000")
elif x <= b:
    print(f"{c / (b - a):.12f}")
else:
    print(f"0.000000000000")
