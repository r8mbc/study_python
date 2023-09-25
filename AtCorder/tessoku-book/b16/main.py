#!/usr/bin/env python3

n = int(input())
H = list(map(int, input().split()))

dp = [0] * n

for i in range(n):
    if i == 0:
        continue
    elif i == 1:
        dp[i] = abs(H[i] - H[0])
    else:
        dp[i] = min(dp[i - 1] + abs(H[i - 1] - H[i]), dp[i - 2] + abs(H[i - 2] - H[i]))

print(dp[-1])
