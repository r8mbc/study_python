#!/usr/bin/env python3

n = int(input())

A = list(map(int, input().split()))

for i in range(n):
    for j in range(n):
        for k in range(n):
            if i == j or j == k or i == k:
                continue
            if A[i] + A[j] + A[k] == 1000:
                print("Yes")
                exit()

print("No")
