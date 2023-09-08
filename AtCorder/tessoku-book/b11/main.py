#!/usr/bin/env python3

import bisect

n = int(input())
A = list(map(int, input().split()))
sortA = sorted(A)
q = int(input())

for _ in range(q):
    x = int(input())

    ans = bisect.bisect_left(sortA,x)
    print(ans)
