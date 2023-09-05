#!/usr/bin/env python3

h, w, n = map(int, input().split())

X = [([0] * (w + 2)) for _ in range(h + 2)]

for _ in range(n):
    a, b, c, d = map(int, input().split())
    X[a][b] += 1
    X[a][d + 1] -= 1
    X[c + 1][b] -= 1
    X[c + 1][d + 1] += 1

for i in range(h + 2):
    now = 0
    for j in range(w + 2):
        now += X[i][j]
        X[i][j] = now

for i in range(w + 2):
    now = 0
    for j in range(h + 2):
        now += X[j][i]
        X[j][i] = now

for i in range(1, h + 1):
    print(*X[i][1:-1])
