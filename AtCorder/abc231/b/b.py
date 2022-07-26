#!/usr/bin/env python3

from collections import Counter


n = int(input())

S = [str(input()) for _ in range(n)]

d = Counter(S)

print(max(d, key=d.get))
