#!/usr/bin/env python3

oct_n, k = map(int, input().split())


def Base_10_to_n(a, b):
    c = ""
    if a == 0:
        c = "0"
    else:
        while a > 0:
            d = str(a % b)
            c = d + c
            a //= b
    return c


for _ in range(k):
    x_n = int(str(oct_n), 8)
    nine_n = Base_10_to_n(x_n, 9)
    oct_n = nine_n.replace("8", "5")

print(oct_n)
