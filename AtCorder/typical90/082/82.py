#!/usr/bin/env python3

l, r = map(int, input().split())
mod = 10**9 + 7
count = 0

len_l = len(str(l))
len_r = len(str(r))

for i in range(len_l, len_r + 1):

    bottom = max(l, 10 ** (i - 1)) - 1
    top = min(r, 10**i - 1)

    count += (top * (top + 1) - bottom * (bottom + 1)) // 2 * i
    count %= mod

print(count)
