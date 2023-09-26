#!/usr/bin/env python3


n, s = map(int, input().split())
A = list(map(int, input().split()))

dp = [[None] * (s + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, s + 1):
    dp[0][i] = False

ans = 0
now = 0
for i in range(1, n + 1):

    for j in range(s + 1):
        if j >= A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
            elif dp[i - 1][j - A[i - 1]] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

        if j < A[i - 1]:
            if dp[i - 1][j] == True:
                dp[i][j] = True
            else:
                dp[i][j] = False

if dp[n][s] == False:
    print(-1)
    exit()

t = s
steps = []

for i in range(n - 1, -1, -1):

    if dp[i][t] == True:
        continue
    else:
        t -= A[i]
        steps.insert(0, i + 1)

print(len(steps))
print(*steps)
