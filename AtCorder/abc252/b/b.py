#!/usr/bin/env python3

n, k = map(int, input().split())

A = list(map(int, input().split()))
B = list(map(int, input().split()))

maxYummy = max(A)

for i in range(n):
    if maxYummy == A[i] and i + 1 in B:
        print("Yes")
        exit()

print("No")
