#!/usr/bin/env python3

h, w = map(int, input().split())

X = [list(map(int, input().split())) for _ in range(h)]

q = int(input())

sum_X = [[0] * (w + 1) for _ in range(h + 1)]

for i in range(h):
    k = 0
    for j in range(w):
        k += X[i][j]
        sum_X[i + 1][j + 1] += k

for j in range(w + 1):
    for i in range(h):
        sum_X[i + 1][j] += sum_X[i][j]


for _ in range(q):
    a, b, c, d = map(int, input().split())

    ans = sum_X[c][d] - sum_X[a - 1][d] - sum_X[c][b - 1] + sum_X[a - 1][b - 1]
    print(ans)
