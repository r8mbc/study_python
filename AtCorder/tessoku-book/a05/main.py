#!/usr/bin/env python3

n, k = map(int, input().split())
ans = 0

for i in range(1, n + 1):
    for j in range(1, n + 1):
        a = k - i - j
        if a <= n and 0 < a:
            ans += 1
            continue

print(ans)
