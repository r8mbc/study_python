#!/usr/bin/env python3

s = input()
t = input()

alpha = "abcdefghijklmnopqrstuvwxyz"

n1 = []
n2 = []
for i in s:
    n1.append(alpha.index(i))

for i in t:
    n2.append(alpha.index(i))

k = (n1[0] - n2[0]) % 26

for i in range(len(s)):
    j = (n1[i] - n2[i]) % 26
    if j != k:
        print("No")
        exit()

print("Yes")
