#!/usr/bin/env python3


from bisect import bisect_left


n, q = map(int, input().split())

A = sorted(list(map(int, input().split())))

for _ in range(q):
    x = int(input())
    index = bisect_left(A, x)
    print(n - index)
