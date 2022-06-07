#!/usr/bin/env python3

h, w = map(int, input().split())

A = [list(map(int, input().split())) for _ in range(h)]
B = [list(map(int, input().split())) for _ in range(h)]

count = 0

for i in range(h - 1):
    change = 0
    for j in range(w - 1):
        if A[i][j] != B[i][j]:
            change = A[i][j] - B[i][j]
            A[i][j] = B[i][j]
            A[i][j + 1] -= change
            A[i + 1][j] -= change
            A[i + 1][j + 1] -= change
            count += abs(change)

if A[-1][-1] == B[-1][-1]:
    print("Yes")
    print(count)
else:
    print("No")
