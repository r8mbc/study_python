#!/usr/bin/env python3

n, k = map(int, input().split())

mod = 10**9 + 7

if n >= 2:
    ans = k * (k - 1) * pow(k - 2, n - 2, mod) % mod
    print(ans)
else:
    print(k)
