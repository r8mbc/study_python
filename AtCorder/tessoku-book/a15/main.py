#!/usr/bin/env python3

import bisect

n = int(input())

A = list(map(int, input().split()))

sA = sorted(set(A))

ans = []
for i in range(n):
    bserach = bisect.bisect_left(sA, A[i])
    ans.append(bserach + 1)

print(*ans)
