#!/usr/bin/env python3

n = int(input())
X = [[] for _ in range(n)]
maxX = 0
maxY = 0

for i in range(n):
    xx, yy = map(int, input().split())

    maxX = max(maxX, xx)
    maxY = max(maxY, yy)

    X[i].append(xx)
    X[i].append(yy)

T = [([0] * (maxX + 1)) for _ in range(maxY + 1)]

for i in X:
    T[i[1]][i[0]] += 1

sum_X = [([0] * (maxX + 1)) for _ in range(maxY + 1)]

for i in range(maxY + 1):
    k = 0
    for j in range(maxX + 1):
        k += T[i][j]
        sum_X[i][j] += k

for i in range(maxX + 1):
    k = 0
    for j in range(maxY):
        sum_X[j + 1][i] += sum_X[j][i]

q = int(input())

for _ in range(q):
    a, b, c, d = map(int, input().split())
    ans = sum_X[d][c] - sum_X[b - 1][c] - sum_X[d][a - 1] + sum_X[b - 1][a - 1]
    print(ans)
