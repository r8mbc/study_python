#!/usr/bin/env python3

n = int(input())

P = [input().split() for _ in range(n)]

x = [int(P[i][0]) for i in range(n)]
y = [int(P[i][1]) for i in range(n)]

s = input()


def Yes():
    print("Yes")
    exit(0)


r_min = dict()
l_max = dict()

for i in range(n):
    if s[i] == "R":
        if y[i] in r_min:
            r_min[y[i]] = min(x[i], r_min[y[i]])
        else:
            r_min[y[i]] = x[i]
    else:
        if y[i] in l_max:
            l_max[y[i]] = max(x[i], l_max[y[i]])
        else:
            l_max[y[i]] = x[i]

    if s[i] == "R":
        if y[i] in l_max and x[i] < l_max[y[i]]:
            Yes()
    else:
        if y[i] in r_min and x[i] > r_min[y[i]]:
            Yes()

print("No")
