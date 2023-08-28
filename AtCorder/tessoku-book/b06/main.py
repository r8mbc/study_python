#!/usr/bin/env python3

n = int(input())

A = list(map(int, input().split()))

sum_A = [0]
now = 0
for i in range(n):
    now += A[i]
    sum_A.append(now)

q = int(input())

for _ in range(q):
    l, r = map(int, input().split())

    # あたり
    c = sum_A[r] - sum_A[l - 1]
    # はずれ
    b = r - l + 1 - c

    if b > c:
        print("lose")
    elif c > b:
        print("win")
    else:
        print("draw")
