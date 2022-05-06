#!/usr/bin/env python3

from collections import Counter

n, m = map(int, input().split())

A = []
B = []

for _ in range(m):
    a, b = sorted(map(int, input().split()))
    B.append(b)

c = 0

for v in Counter(B).values():
    if v == 1:
        c += 1

print(c)
