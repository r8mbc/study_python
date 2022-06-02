#!/usr/bin/env python3

n, k = map(int, input().split())

A = [0] * n
B = [0] * n
C = [0] * n

for i in range(n):
    x, y = map(int, input().split())
    A[i] = x
    B[i] = y
    C[i] = x - y

A = sorted(A)
B = sorted(B)
D = sorted(B + C)

print(sum(D[-k:]))
