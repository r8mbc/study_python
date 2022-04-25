#!/usr/bin/env python3

n = int(input())

c1 = [0] * n
c2 = [0] * n

for i in range(n):
    c, p = map(int, input().split())
    if c == 1:
        c1[i] = p
    else:
        c2[i] = p

s1 = [0] * (n + 1)
s2 = [0] * (n + 1)

for i in range(n):
    s1[i + 1] = s1[i] + c1[i]
    s2[i + 1] = s2[i] + c2[i]

for _ in range(int(input())):
    L, R = map(int, input().split())
    ans1 = s1[R] - s1[L - 1]
    ans2 = s2[R] - s2[L - 1]
    print(ans1, ans2)
