#!/usr/bin/env python3

n, w = map(int, input().split())

A = [0]
V = [0]

for _ in range(n):
    i, j = map(int, input().split())
    A.append(i)
    V.append(j)

dp = [[10**15] * (100001) for _ in range(n + 1)]
dp[0][0] = 0

for i in range(1, n + 1):
    for j in range(100001):
        if j < V[i]:
            dp[i][j] = dp[i - 1][j]
        if j >= V[i]:
            dp[i][j] = min(dp[i - 1][j], dp[i - 1][j - V[i]] + A[i])


ans = 0
for i in range(100001):
    if dp[n][i] <= w:
        ans = i

print(ans)
