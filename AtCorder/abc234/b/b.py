#!/usr/bin/env python3

from math import sqrt
from itertools import combinations

n = int(input())

XY = list(list(map(int, input().split())) for _ in range(n))

ans = 0

for i in combinations(XY, 2):
    ans = max(ans, (i[0][0] - i[1][0]) ** 2 + (i[0][1] - i[1][1]) ** 2)

print(sqrt(ans))
