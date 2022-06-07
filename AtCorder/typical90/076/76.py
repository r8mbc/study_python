#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))
ten = sum(A) // 10
A += A

if ten < 1:
    print("No")
    exit(0)

ans = 0
j = 0
for i in range(n + 1):
    while ans < ten:
        ans += A[j]
        j += 1
    if ans == ten:
        print("Yes")
        exit()
    if j == i:
        j += 1
    ans -= A[i]

print("No")
