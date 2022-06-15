#!/usr/bin/env python3


x1, y1, x2, y2 = map(int, input().split())

knight = [(1, 2), (2, 1), (-1, 2), (-2, 1), (1, -2), (2, -1), (-1, -2), (-2, -1)]

for i in knight:
    for j in knight:
        if x1 + i[0] + j[0] == x2 and y1 + i[1] + j[1] == y2:
            print("Yes")
            exit()

print("No")
