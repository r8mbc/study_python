#!/usr/bin/env python3

from collections import Counter

n = int(input())

A = list(map(int, input().split()))
B = list(map(int, input().split()))
C = list(map(int, input().split()))

for i in range(n):
    A[i] %= 46
    B[i] %= 46
    C[i] %= 46

cntA = Counter(A)
cntB = Counter(B)
cntC = Counter(C)

count = 0
for i in cntA.keys():
    for j in cntB.keys():
        for h in cntC.keys():
            if (i + j + h) % 46 == 0:
                count += cntA[i] * cntB[j] * cntC[h]
print(count)
