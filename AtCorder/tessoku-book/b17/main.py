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

ans = []
now = n
while True:

    ans.insert(0, now)

    if now <= 1:
        break

    if dp[now - 1] == dp[now - 2] + abs(H[now - 2] - H[now - 1]):
        now -= 1

    elif dp[now - 1] == dp[now - 3] + abs(H[now - 3] - H[now - 1]):
        now -= 2


print(len(ans))
print(*ans)
