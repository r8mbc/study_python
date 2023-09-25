#!/usr/bin/env python3

import bisect

n, k = map(int, input().split())

A = list(map(int, input().split()))

m = n // 2

maeA = A[:m]
atoA = A[m:]

maeAA = []
atoAA = []


for i in range(2 ** len(maeA)):
    s = 0
    for j in range(len(maeA)):
        if i & (1 << j):
            s += maeA[j]
    maeAA.append(s)


for i in range(2 ** len(atoA)):
    s = 0
    for j in range(len(atoA)):
        if i & (1 << j):
            s += atoA[j]
    atoAA.append(s)

maeAA.sort()
atoAA.sort()

for i in maeAA:
    bserach = bisect.bisect_left(atoAA, k - i)
    if bserach < len(atoAA) and k - i == atoAA[bserach]:
        print("Yes")
        exit()

print("No")
