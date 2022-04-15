#!/usr/bin/env python3

n = int(input())

P = [input().split() for _ in range(n)]

x = [int(P[i][0]) for i in range(n)]
y = [int(P[i][1]) for i in range(n)]

s = input()


def Yes():
    print("Yes")
    exit(0)


if len(set(s)) == 1 or len(set(y)) == n:
    print("No")
    exit(0)

print("No")
