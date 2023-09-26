#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


dp = [0] * n
ans = []

for i in range(n):
    if i == 0:
        continue
    if i == 1:
        dp[i] = A[0]
    else:
        dp[i] = min(dp[i - 1] + A[i - 1], dp[i - 2] + B[i - 2])

now = n

while True:
    ans.append(now)

    if now == 1:
        break

    if dp[now - 1] == dp[now - 2] + A[now - 2]:
        now -= 1
    elif dp[now - 1] == dp[now - 3] + B[now - 3]:
        now -= 2

ans.reverse()

print(len(ans))
print(*ans)
