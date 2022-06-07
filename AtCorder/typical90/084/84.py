#!/usr/bin/env python3


n = int(input())
s = str(input())

count = n * (n + 1) // 2

only_o = s.split("x")
only_x = s.split("o")

for i in only_o:
    count -= len(i) * (len(i) + 1) // 2

for i in only_x:
    count -= len(i) * (len(i) + 1) // 2

print(count)
