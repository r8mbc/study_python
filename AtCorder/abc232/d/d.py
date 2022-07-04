#!/usr/bin/env python3

INF = 10**6

h, w = map(int, input().split())
C = [input() for _ in range(h)]

dp = [[-INF] * w for _ in range(h)]
dp[0][0] = 1

for i in range(h):
    for j in range(w):

        if i == j == 0:
            continue

        if C[i][j] == ".":

            if i - 1 >= 0:
                a = dp[i - 1][j]
            else:
                a = -INF

            if j - 1 >= 0:
                b = dp[i][j - 1]
            else:
                b = -INF

            dp[i][j] = max(a, b) + 1

ans = 1

for d in dp:
    ans = max(ans, *d)

print(ans)
