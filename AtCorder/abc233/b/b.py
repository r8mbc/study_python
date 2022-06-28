#!/usr/bin/env python3

l, r = map(int, input().split())
s = str(input())

aida = s[l - 1 : r]

print(s[: l - 1] + aida[::-1] + s[r:])
