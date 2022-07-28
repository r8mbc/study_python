#!/usr/bin/env python3

n = int(input())

if n < 42:
    n = str(n).zfill(3)
else:
    n += 1
    n = str(n).zfill(3)

print("AGC" + n)
