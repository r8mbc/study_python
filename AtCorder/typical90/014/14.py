#!/usr/bin/env python3

n = int(input())
A = map(int, input().split())
B = map(int, input().split())

A = sorted(A)
B = sorted(B)

res = 0

for i in range(n):
    res += abs(A[i] - B[i])

print(res)
