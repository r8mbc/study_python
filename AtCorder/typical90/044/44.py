#!/usr/bin/env python3

from collections import deque

n, q = map(int, input().split())

A = deque(input().split())

for _ in range(q):

    t, x, y = map(int, input().split())

    if t == 1:
        A[x - 1], A[y - 1] = A[y - 1], A[x - 1]
    elif t == 2:
        A.rotate()
    else:
        print(A[x - 1])

