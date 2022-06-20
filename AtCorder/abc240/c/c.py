#!/usr/bin/env python3

n, x = map(int, input().split())

A = [0] * n
B = [0] * n
for i in range(n):
    c, d = map(int, input().split())
    A[i] = c
    B[i] = d

dp = [[False] * (x + 1) for _ in range(n + 1)]
dp[0][0] = True

for i in range(n):
    for j in range(x + 1):
        if dp[i][j]:
            if j + A[i] <= x:
                dp[i + 1][j + A[i]] = True
            if j + B[i] <= x:
                dp[i + 1][j + B[i]] = True

if dp[n][x]:
    print("Yes")
else:
    print("No")
