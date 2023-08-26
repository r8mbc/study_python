#!/usr/bin/env python3

N = str(input())

ans = 0
X = []
for i in range(len(N)):
    X.insert(0, 2**i)

for i in range(len(N)):
    ans += X[i] * int(N[i])

print(ans)
