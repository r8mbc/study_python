#!/usr/bin/env python3

n = int(input())


l = 0.0
r = 100.0
x = 0

for _ in range(20):
    middle = (l + r) / 2
    x = middle**3 + middle

    if n == x:
        print(middle)
        exit()
    elif n > x:
        l = middle
    else:
        r = middle

print(middle)
