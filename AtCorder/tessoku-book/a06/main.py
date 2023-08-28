#!/usr/bin/env python3

n, p = map(int, input().split())

A = list(map(int, input().split()))

sum_A = [0]
now = 0

for i in range(n):
    now += A[i]
    sum_A.append(now)

for _ in range(p):
    l, r = map(int, input().split())
    print(sum_A[r] - sum_A[l - 1])
