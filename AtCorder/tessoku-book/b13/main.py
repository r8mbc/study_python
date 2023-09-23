#!/usr/bin/env python3

n, k = map(int, input().split())

A = list(map(int, input().split()))

B = [0] * n
ans = 0


def total_sum(l, r, D):
    return D[r + 1] - D[l]


C = [0] * (n + 1)
for i in range(1, n + 1):
    C[i] = C[i - 1] + A[i - 1]


for i in range(n):
    if i != 0:
        B[i] = B[i - 1]
    else:
        B[i] = -1

    while B[i] + 1 < n and total_sum(i, B[i] + 1, C) <= k:
        B[i] += 1

    ans += B[i] - i + 1

print(ans)
