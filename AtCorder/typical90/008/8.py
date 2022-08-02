#!/usr/bin/env python3

n = int(input())
s = input()

at = "atcoder"

mod = 10**9 + 7

dp = [[0] * 8 for _ in range(n + 1)]

for i in range(n + 1):
    dp[i][0] = 1

for i in range(n):
    for j in range(7):
        if s[i] == at[j]:
            dp[i + 1][j + 1] = dp[i][j] + dp[i][j + 1]
        else:
            dp[i + 1][j + 1] = dp[i][j + 1]

        dp[i + 1][j + 1] %= mod

print(dp[n][7])
