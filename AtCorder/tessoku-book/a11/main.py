#!/usr/bin/env python3

n, x = map(int, input().split())
A = list(map(int, input().split()))

l = 0
r = n

for _ in range(n):
    m = (l + r) // 2
    if x == A[m]:
        print(m + 1)
        exit()
    elif x < A[m]:
        r = m
        continue
    elif x > A[m]:
        l = m
