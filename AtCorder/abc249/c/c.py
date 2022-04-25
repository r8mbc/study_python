#!/usr/bin/env python3

n, k = map(int, input().split())

S = list(input() for _ in range(n))

alpha = ""
for i in S:
    alpha += i

alphalen = len(set(alpha))

a = 'qwertyuiopasdfghjklzxcvbnm'

print(alpha)
