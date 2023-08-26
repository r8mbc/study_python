#!/usr/bin/env python3

n = int(input())
X = []

for i in range(10):
    X.append(2**i)

ans = []
for i in range(1, 11):
    ans.append(str((n // X[-i]) % 2))

print("".join(ans))
