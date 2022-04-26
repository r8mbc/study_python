#!/usr/bin/env python3

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))


def even(c):
    if c % 2 == 0:
        print("Yes")
        exit(0)
    else:
        print("No")
        exit(0)

use = 0
for i in range(len(A)):
    use += abs(A[i] - B[i])

if k - use >= 0:
    even(k - use)
else:
    print("No")
