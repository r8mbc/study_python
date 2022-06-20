#!/usr/bin/env python3


n = int(input())
H = list(map(int, input().split()))

now = H[0]

for i in range(1, n):
    if now < H[i]:
        now = H[i]
    else:
        print(now)
        exit()

print(now)