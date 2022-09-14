#!/usr/bin/env python3

from collections import defaultdict

n, k = map(int, input().split())
maxi = n - k

A = list(map(int, input().split()))

goalA = sorted(A)

count = defaultdict(int)

for i in range(k):

    b = 0
    while i + k * b < n:
        count[A[i + k * b]] += 1
        b += 1

    b = 0
    while i + k * b < n:
        count[goalA[i + k * b]] -= 1

        if count[goalA[i + k * b]] < 0:
            print("No")
            exit()

        b += 1

print("Yes")
