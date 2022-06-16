#!/usr/bin/env python3

S = input()

aleft = len(S) - len(S.lstrip("a"))
aright = len(S) - len(S.rstrip("a"))

if aleft > aright:
    print("No")
    exit()
else:
    Sa = "a" * (aright - aleft) + S

if Sa == Sa[::-1]:
    print("Yes")
else:
    print("No")
