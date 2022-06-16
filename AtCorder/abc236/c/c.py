#!/usr/bin/env python3

n, m = map(int, input().split())

S = list(map(str, input().split()))
T = list(map(str, input().split()))

for i in range(n):
    if S[i] == T[0]:
        print("Yes")
        T.pop(0)
    else:
        print("No")
