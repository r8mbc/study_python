#!/usr/bin/env python3

from itertools import combinations

n, w = map(int, input().split())
A = list(map(int, input().split()))

count = set()

for j in range(1, min(n + 1, 4)):
    for i in combinations(A, j):
        if sum(i) <= w:
            count.add(sum(i))

print(len(count))
