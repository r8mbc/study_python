#!/usr/bin/env python3


n = int(input())
A = [input().split() for _ in range(n)]

B = []

for i in A:
    for j in i:
        B.append(j)


def func():
    for i in A:
        if i[0] == i[1]:
            myozi = B.count(i[0])
            namae = B.count(i[1])
            if myozi != 2:
                if namae != 2:
                    return "No"
        else:
            myozi = B.count(i[0])
            namae = B.count(i[1])
            if myozi != 1:
                if namae != 1:
                    return "No"
    return "Yes"


print(func())
