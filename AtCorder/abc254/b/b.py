#!/usr/bin/env python3

n = int(input())

before = [1, 1]

if n == 1:
    print(1)
    exit()
elif n == 2:
    print(1)
    print("1 1")
    exit()
else:
    print(1)
    print("1 1")
    for j in range(n - 2):
        now = [before[0]]

        for i in range(len(before) - 1):
            now.append(before[i] + before[i + 1])

        now.append(before[-1])

        print(*now)

        before = now
