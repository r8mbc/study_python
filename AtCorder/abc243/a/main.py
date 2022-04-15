#!/usr/bin/env python3

v, a, b, c = map(int, input().split())
count = 0

while v >= 0:
    if v >= 0:
        turn = "F"
        v -= a
    if v >= 0:
        turn = "M"
        v -= b
    if v >= 0:
        turn = "T"
        v -= c

print(turn)
