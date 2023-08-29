#!/usr/bin/env python3

d = int(input())
n = int(input())

Z = [0] * d

for _ in range(n):
    l, r = map(int, input().split())
    Z[l - 1] += 1
    if r == d:
        continue
    Z[r] -= 1

ans = 0

for i in Z:
    ans += i
    print(ans)
