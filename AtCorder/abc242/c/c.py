#!/usr/bin/env python3

import sys

input = sys.stdin.readline


def func():
    n = int(input())
    s = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1]
    mod = 998244353

    for _ in range(1, n):
        m = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        m[0] = s[0] + s[1] % mod
        m[1] = s[0] + s[1] + s[2] % mod
        m[2] = s[1] + s[2] + s[3] % mod
        m[3] = s[2] + s[3] + s[4] % mod
        m[4] = s[3] + s[4] + s[5] % mod
        m[5] = s[4] + s[5] + s[6] % mod
        m[6] = s[5] + s[6] + s[7] % mod
        m[7] = s[6] + s[7] + s[8] % mod
        m[8] = s[7] + s[8] % mod
        s = m

    return sum(s) % mod


print(func())
