#!/usr/bin/env python3


from collections import defaultdict

n, q = map(int, input().split())

A = list(map(int, input().split()))

D = defaultdict(list)

for i in range(n):
    D[A[i]].append(i)

for i in range(q):
    x, k = map(int, input().split())

    if x in D:
        if k <= len(D[x]):
            print(D[x][k - 1] + 1)
        else:
            print(-1)
    else:
        print(-1)
