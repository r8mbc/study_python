#!/usr/bin/env python3


n = int(input())

w = 1500
h = 1500

X = [([0] * (w + 1)) for _ in range(h + 1)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    X[a][b] += 1
    X[a][d] -= 1
    X[c][b] -= 1
    X[c][d] += 1

for i in range(h + 1):
    now = 0
    for j in range(w + 1):
        now += X[i][j]
        X[i][j] = now

for i in range(w + 1):
    now = 0
    for j in range(h + 1):
        now += X[j][i]
        X[j][i] = now

ans = 0
for i in range(h):
    for j in range(w):
        if X[i][j] > 0:
            ans += 1
print(ans)

# for i in range(1, h + 1):
#     print(*X[i][1:-1])
