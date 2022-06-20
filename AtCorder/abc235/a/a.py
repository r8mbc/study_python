#!/usr/bin/env python3

x = str(input())

a = x[0]
b = x[1]
c = x[2]

print(int(a + b + c) + int(b + c + a) + int(c + a + b))
