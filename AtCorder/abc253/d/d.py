#!/usr/bin/env python3

from math import gcd

n, a, b = map(int, input().split())

all = sum(range(1, n + 1))

a_ko = n // a
b_ko = n // b

ab = a * b // gcd(a, b)

ab_ko = n // ab


def solve(c, d):
    s = ((c + 1) * c) // 2
    return s * d


print(all - solve(a_ko, a) - solve(b_ko, b) + solve(ab_ko, ab))
