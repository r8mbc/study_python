#!/usr/bin/env python3

t = int(input())
n = int(input())

Z = [0] * (t)

for _ in range(n):
    l, r = map(int, input().split())
    Z[l] += 1
    if r == t:
        continue
    Z[r] -= 1

ans = 0

for i in Z:
    ans += i
    print(ans)

# print(Z)