#!/usr/bin/env python3

from math import sqrt


n, k = map(int, input().split())

A = list(map(int, input().split()))

for i in range(k):
    A[i] -= 1

XY = list(list(map(int, input().split())) for _ in range(n))

minimu = []

for i in range(n):
    distance = []
    for j in A:
        distance.append((XY[i][0] - XY[j][0]) ** 2 + (XY[i][1] - XY[j][1]) ** 2)

    minimu.append(min(distance))

print(sqrt(max(minimu)))
