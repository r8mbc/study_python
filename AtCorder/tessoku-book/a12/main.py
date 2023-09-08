#!/usr/bin/env python3


def check(middle, n, A, k):
    now = 0
    for i in range(n):
        now += middle // A[i]

    if now >= k:
        return True
    return False


n, k = map(int, input().split())
A = list(map(int, input().split()))

l = 1
r = 10**9

while l < r:
    m = (l + r) // 2
    ans = check(m, n, A, k)

    if ans:
        r = m
    else:
        l = m + 1

print(l)
