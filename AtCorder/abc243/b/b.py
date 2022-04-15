#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

k = 0

for i in range(n):
    if A[i] == B[i]:
        k += 1

print(k)
print(len(set(A) & set(B)) - k)
