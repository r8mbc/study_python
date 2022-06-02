#!/usr/bin/env python3

n, q = map(int, input().split())

A = list(map(int, input().split()))
SA = [0] * n

for i in range(1, n):
    SA[i - 1] = A[i] - A[i - 1]

s = sum(abs(i) for i in SA)

for _ in range(q):
    l, r, v = map(int, input().split())
    l -= 1
    r -= 1

    before = abs(SA[l - 1]) + abs(SA[r])

    if l != 0:
        SA[l - 1] += v

    if r != n - 1:
        SA[r] -= v

    after = abs(SA[l - 1]) + abs(SA[r])

    s += after - before

    print(s)
