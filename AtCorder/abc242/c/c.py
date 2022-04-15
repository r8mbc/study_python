#!/usr/bin/env python3

n = int(input())

ans = 9
m = 2

for i in range(n - 1):
    ans *= 3

for i in range(n - 1):
    m *= 3

print(ans, m)
