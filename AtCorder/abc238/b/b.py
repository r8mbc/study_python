#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

pai = 360
big = A[0]
B = [0, 360]
d = 0
for i in range(n):
    d += A[i]
    d %= 360
    B.append(d)

B.sort()

C = []

if n == 1:
    C = [360 - A[0], A[0]]

else:
    for i in range(1, n):
        C.append(B[i] - B[i - 1])

print(max(C))
