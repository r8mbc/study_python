#!/usr/bin/env python3

from collections import Counter
from itertools import combinations

n, k = map(int, input().split())

S = list(input() for _ in range(n))

for i in range(n):
    S[i] = Counter(S[i])

ans = 0
for h in range(1, n + 1):
    for j in combinations(S, h):
        sum_s = sum(j, start=Counter())
        count = 0
        for value in sum_s.values():
            if value == k:
                count += 1
        ans = max(ans, count)

print(ans)
