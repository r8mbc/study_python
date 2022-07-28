#!/usr/bin/env python3


n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())


ans = [["."] * n for _ in range(n)]

for i in range(max(1 - a, 1 - b) - 1, min(n - a, n - b)):
    ans[a + i][b + i] = "#"

for j in range(max(1 - a, b - n) - 1, min(n - a, b - 1)):
    ans[a + j][b - j - 2] = "#"

for k in range(p - 1, q):
    print(*ans[k][r - 1 : s], sep="")
