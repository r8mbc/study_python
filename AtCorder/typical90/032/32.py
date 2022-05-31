#!/usr/bin/env python3

from itertools import permutations

n = int(input())

A = [list(map(int, input().split())) for _ in range(n)]

m = int(input())

xy = [[True] * n for _ in range(n)]

for _ in range(m):
    x, y = map(int, input().split())
    xy[x - 1][y - 1] = False
    xy[y - 1][x - 1] = False


runner = [i for i in range(n)]
ans = pow(10, 1000)

for sosha in permutations(runner):

    bool = True
    for i in range(n - 1):
        if xy[sosha[i]][sosha[i + 1]] == False:
            bool = False
            break

    if bool:
        kyori = 0
        for i in range(n):
            kyori += A[sosha[i]][i]
        ans = min(kyori, ans)

if ans == pow(10, 1000):
    print(-1)
else:
    print(ans)
