#!/usr/bin/env python3

n, m, k = map(int, input().split())

dp = list([0] * (k + 1) for _ in range(n + 1))
dp[0][0] = 1

mod = 998244353

for i in range(n):
    for j in range(k):
        for g in range(1, m + 1):
            if j + g > k:
                break

            dp[i + 1][j + g] += dp[i][j]
            dp[i + 1][j + g] %= mod

print(sum(dp[-1]) % mod)

