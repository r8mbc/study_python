#!/usr/bin/env python3

q = int(input())

A = []

for _ in range(q):
    t, x = map(int, input().split())
    if t == 1:
        A.insert(0, x)
    elif t == 2:
        A.append(x)
    else:
        print(A[x - 1])
