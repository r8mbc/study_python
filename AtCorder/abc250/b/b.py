#!/usr/bin/env python3

n, a, b = map(int, input().split())

first = ""
second = ""

for i in range(n):
    if i % 2 == 0:
        first += "." * b
        second += "#" * b
    else:
        first += "#" * b
        second += "." * b

for i in range(n):
    if i % 2 == 0:
        for _ in range(a):
            print(first)
    else:
        for _ in range(a):
            print(second)
