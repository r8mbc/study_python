#!/usr/bin/env python3

h, w = map(int, input().split())

if h == 1 or w == 1:
    print(max(h, w))
    exit(0)

yoko = w - w // 2
tate = h - h // 2

print(yoko * tate)
