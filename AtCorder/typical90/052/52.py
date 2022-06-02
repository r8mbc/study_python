#!/usr/bin/env python3

n = int(input())
mod = 10**9 + 7

A = [list(map(int, input().split())) for _ in range(n)]
S = [0] * n

ans = 1

for i in range(n):
    S[i] = sum(A[i]) % mod

for i in S:
    ans *= i
    ans %= mod

print(ans)
