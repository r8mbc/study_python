#!/usr/bin/env python3

n, w = map(int, input().split())

A = [0]
V = [0]

for _ in range(n):
    i, j = map(int, input().split())
    A.append(i)
    V.append(j)

dp = [[0] * (w + 1) for _ in range(n + 1)]
# dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(w + 1):
        if j < A[i]:
            dp[i][j] = dp[i - 1][j]
        if j >= A[i]:
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - A[i]] + V[i])

print(max(dp[n]))
