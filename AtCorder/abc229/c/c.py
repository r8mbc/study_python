#!/usr/bin/env python3

n, w = map(int, input().split())

AB = [[0, 0] for _ in range(n)]


for i in range(n):
    x, y = map(int, input().split())
    AB[i][0] = x
    AB[i][1] = y

AB = sorted(AB, reverse=True)

now = 0
for i in AB:
    if i[1] <= w:
        w -= i[1]
        now += i[0] * i[1]
    else:
        now += i[0] * w
        print(now)
        exit()

print(now)
