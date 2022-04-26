#!/usr/bin/env python3

from math import gcd

a, b, c = map(int, input().split())

# gcd 関数を使った場合
# g = gcd(a, b)
# g = gcd(g, c)

# お手製で計算した場合
def func(g1, g2):
    while g2 > 0:
        g1, g2 = g2, g1 % g2
    return g1

g = func(a, b)
g = func(c, g)

ans = (a // g) + (b // g) + (c // g) - 3

print(ans)
