#!/usr/bin/env python3

n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())

for k in range(p, q + 1):
    ans = ["."] * (s + 1 - r)
    for i in range(r, s + 1):
        if (k - i == a - b) or (k + i == a + b):
            ans[i - r] = "#"
    print(*ans, sep="")
