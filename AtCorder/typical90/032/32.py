#!/usr/bin/env python3

from itertools import permutations

n = int(input())

A = [input().split() for _ in range(n)]

m = int(input())

xy = [input().split() for _ in range(m)]

runner = [i for i in range(1, n + 1)]
ans = pow(10, 1000)

for sosha in permutations(runner):
    kyori = 0
    for i in sosha:
        for j in range(n):
            kyori += A[i][j]
