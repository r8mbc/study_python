#!/usr/bin/env python3

a, b, c, d = map(int, input().split())

takahashi = list(range(a, b + 1))
aoki = list(range(c, d + 1))

sosu = [
    2,
    3,
    5,
    7,
    11,
    13,
    17,
    19,
    23,
    29,
    31,
    37,
    41,
    43,
    47,
    52,
    59,
    61,
    67,
    71,
    73,
    79,
    83,
    89,
    97,
    101,
    107,
    109,
    113,
    127,
    131,
    137,
    139,
    149,
    151,
    157,
    163,
    167,
    173,
    179,
    181,
    191,
    193,
    197,
    199,
]

for i in takahashi:
    count = 0
    for j in aoki:
        if i + j in sosu:
            count += 1
    if count == 0:
        print("Takahashi")
        exit()
    else:
        continue

print("Aoki")
