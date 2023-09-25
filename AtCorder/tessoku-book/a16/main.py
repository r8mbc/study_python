#!/usr/bin/env python3

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        continue
    if i == 1:
        dp[i] = A[0]
    else:
        dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

print(dp[-1])
