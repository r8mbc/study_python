#!/usr/bin/env python3

import bisect

n = int(input())

A = sorted(list(map(int, input().split())))
q = int(input())

for i in range(q):
    b = int(input())

    insert_index = bisect.bisect_left(A, b)

    if insert_index == n:
        ans = abs(A[-1] - b)
    elif insert_index == 0:
        ans = abs(A[0] - b)
    else:
        ans = min(abs(A[insert_index - 1] - b), abs(A[insert_index] - b))
    print(ans)
