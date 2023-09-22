#!/usr/bin/env python3

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = [0] * n

ans = 0

for i in range(n - 1):

    if i != 0:
        B[i] = B[i - 1]

    while (B[i] + 1 < n) and (A[B[i] + 1] - A[i] <= k):
        B[i] += 1

    ans += B[i] - i

print(ans)
