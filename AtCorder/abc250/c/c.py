#!/usr/bin/env python3

n, q = map(int, input().split())

idx = [i for i in range(n + 1)]
A = [i for i in range(n + 1)]

for i in range(q):
    x = int(input())

    doko = idx[x]
    if doko == n:
        change = doko - 1
    else:
        change = doko + 1

    y = A[change]

    A[doko], A[change] = A[change], A[doko]

    idx[x] = change
    idx[y] = doko

print(*A[1:])
