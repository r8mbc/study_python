#!/usr/bin/env python3

n = int(input())

A = set()

for i in range(n):
    name = str(input())
    if name not in A:
        A.add(name)
        print(i + 1)
