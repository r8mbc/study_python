#!/usr/bin/env python3

t = int(input())


def solve(a):
    ans = a**2 + 2 * a + 3
    return ans


print(solve(solve(solve(t) + t) + solve(solve(t))))
