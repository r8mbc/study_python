#!/usr/bin/env python3

s1 = input()
s2 = input()

if (s1 == ".." or s2 == "..") or (s1 == "##" or s2 == "##") or (s1 == s2):
    print("Yes")
else:
    print("No")
