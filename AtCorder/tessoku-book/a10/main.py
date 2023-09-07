#!/usr/bin/env python3

n = int(input())

A = list(map(int, input().split()))
A.insert(0, 0)

d = int(input())

now = 0
leftA = []
for i in range(n):
    now = max(A[i], now)
    leftA.append(now)

now = 0
rightA = []
for i in range(n, 0, -1):
    now = max(A[i], now)
    rightA.insert(0, now)

# print(leftA)
# print(rightA)

for _ in range(d):
    l, r = map(int, input().split())
    print(max(leftA[l - 1], rightA[r]))
