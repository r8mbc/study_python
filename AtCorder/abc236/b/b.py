#!/usr/bin/env python3

from collections import Counter

n = int(input())
A = map(int, input().split())

d = Counter(A)

for k, v in d.items():
    if v == 3:
        print(k)
