#!/usr/bin/env python3


def func():

    n, m = map(int, input().split())
    A = sorted(list(input().split()))
    B = sorted(list(input().split()))

    for i in range(m):
        if B[i] in A:
            A.remove(B[i])
        else:
            return "No"
    return "Yes"


print(func())
