#!/usr/bin/env python3

h, w = map(int, input().split())

A = list(list(map(int, input().split())) for _ in range(h))

B = []
C = []
ans = []

for i in range(h):
    B.append(sum(A[i]))

for i in range(w):
    tate = 0
    for j in range(h):
        tate += A[j][i]
    C.append(tate)

for i in range(h):
    sublist = []
    for j in range(w):
        sublist.append(B[i] + C[j] - A[i][j])
    ans.append(sublist)

for i in ans:
    print(*i)
