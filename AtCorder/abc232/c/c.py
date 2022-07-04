#!/usr/bin/env python3

from itertools import permutations


def judge():

    n, m = map(int, input().split())

    AB = [[False] * n for _ in range(n)]
    CD = [[False] * n for _ in range(n)]

    if m == 0:
        return True

    for _ in range(m):
        a, b = map(int, input().split())
        a, b = a - 1, b - 1
        AB[a][b] = True
        AB[b][a] = True

    for _ in range(m):
        c, d = map(int, input().split())
        c, d = c - 1, d - 1
        CD[c][d] = True
        CD[d][c] = True

    def solve(g):
        for i in range(n):
            for j in range(n):
                if AB[g[i]][g[j]] != CD[i][j]:
                    return False
        return True

    for pre in permutations(range(n)):
        if solve(pre):
            return True
    return False


if judge():
    print("Yes")
else:
    print("No")
