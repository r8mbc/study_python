#!/usr/bin/env python3

s = str(input())

if not s.isupper():
    if not s.islower():
        if len(s) == len(set(s)):
            print("Yes")
        else:
            print("No")
    else:
        print("No")
else:
    print("No")
