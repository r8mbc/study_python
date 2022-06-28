#!/usr/bin/env python3

from collections import defaultdict
from itertools import accumulate

n, k = map(int, input().split())

A = [0] + list(map(int, input().split()))
dist = defaultdict(int)

count = 0

for j in accumulate(A):
    b = j - k
    count += dist[b]
    dist[j] += 1

print(count)
