#!/usr/bin/env python3

from itertools import combinations

n, p, q = map(int, input().split())
A = list(map(int, input().split()))

count = 0

if len(A) == 5:
    if (A[0] % p * A[1] % p * A[2] % p * A[3] % p * A[4] % p) % p == q:
        print(1)
        exit(0)
    else:
        print(0)
        exit(0)

for i in combinations(A, 5):
    prod = i[0] % p * i[1] % p * i[2] % p * i[3] % p * i[4] % p
    if prod % p == q:
        count += 1

print(count)
