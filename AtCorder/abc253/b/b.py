#!/usr/bin/env python3

h, w = map(int, input().split())

S = [input() for _ in range(h)]

yoko = []
tate = []

for i in range(h):
    if "o" in S[i]:
        for j in range(len(S[i])):
            if S[i][j] == "o":
                yoko.append(j)
                tate.append(i)

if yoko[0] == yoko[1]:
    print(abs(tate[1] - tate[0]))
else:
    if tate[0] == tate[1]:
        print(abs(yoko[1] - yoko[0]))
    else:
        print(abs(tate[1] - tate[0]) + abs(yoko[1] - yoko[0]))
