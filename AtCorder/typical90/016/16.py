#!/usr/bin/env python3

n = int(input())
A = sorted(map(int, input().split()), reverse=True)

use1 = n // A[0]
use2 = n // A[1]

res = 9999

if A[1] > n:
    print(n // A[2])
    exit(0)
elif A[0] > n:
    for j in range(use2):
        change = n
        if change >= A[1] * j:
            change -= A[1] * j
        if change % A[2] == 0:
            res = min(res, j + change // A[2])
else:
    for i in range(use1, 0, -1):
        for j in range(use2):
            change = n - A[0] * i
            if change >= A[1] * j:
                change -= A[1] * j
            if change % A[2] == 0:
                res = min(res, i + j + change // A[2])

print(res)
