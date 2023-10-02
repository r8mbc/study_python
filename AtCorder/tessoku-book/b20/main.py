#!/usr/bin/env python3

s = str(input())
t = str(input())

ns = len(s) + 1
nt = len(t) + 1

dp = [[0] * ns for _ in range(nt)]

# for i in range(1, ns):
#     dp[0][i] = dp[0][i - 1] + 1

# for j in range(1, nt):
#     dp[j][0] = dp[j - 1][0] + 1

for i in range(nt):
    for j in range(ns):
        if i > 0 and j > 0:
            if s[j - 1] == t[i - 1]:
                dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1])
            else:
                dp[i][j] = min(dp[i - 1][j], dp[i][j - 1], dp[i - 1][j - 1]) + 1
        elif i > 0:
            dp[i][j] = dp[i - 1][j] + 1
        elif j > 0:
            dp[i][j] = dp[i][j - 1] + 1

print(dp[nt-1][ns-1])
