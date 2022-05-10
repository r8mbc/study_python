#!/usr/bin/env python3

h, w = map(int, input().split())
r, c = map(int, input().split())

if h == 1:
    if w == 1:
        print(0)
        exit(0)
    else:
        if c == 1 or c == w:
            print(1)
        else:
            print(2)
elif h == 2:
    if r == 1:
        if c == 1 or c == w:
            print(2)
        else:
            print(3)
    elif r == h:
        if c == 1 or c == w:
            print(2)
        else:
            print(3)
else:
    if w == 1:
        if r == 1 or h == r:
            print(1)
        else:
            print(2)
    elif r == 1:
        if c == 1 or c == w:
            print(2)
        else:
            print(3)
    elif r == h:
        if c == 1 or c == w:
            print(2)
        else:
            print(3)
    else:
        if c == 1 or c == w:
            print(3)
        else:
            print(4)
