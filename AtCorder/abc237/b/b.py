#!/usr/bin/env python3

h, w = map(int, input().split())

A = list(list(map(int, input().split())) for _ in range(h))
B = []

for i in range(w):
    C = []
    for j in range(h):
        C.append(A[j][i])
    B.append(C)

for i in B:
    print(*i)
