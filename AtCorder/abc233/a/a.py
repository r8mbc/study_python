#!/usr/bin/env python3

x, y = map(int, input().split())

if y - x > 0:
    if (y - x) % 10 == 0:
        print((y - x) // 10)
    else:
        print(((y - x) // 10) + 1)
else:
    print(0)
