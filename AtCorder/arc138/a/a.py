#!/usr/bin/env python3

from itertools import product

n, k = map(int, input().split())
A = list(map(int, input().split()))

s = sum(A[:k])


def fun():
    max = sorted(A, reverse=True)
    if sum(max[:k]) > s:
        for i in range(1, n - 1):
            if sum(A[i : i + k]) > s:
                return i
        for i in range(1, n - 1):
    else:
        return -1

    # for i in product(A, repeat=k):
    #     if s < sum(i):
    #         print(i)
    #         for g in range(k):
    #             li = [y for y, x in enumerate(A) if x == i[g]]
    #             count += sum(li)
    #         return count
    # return -1


print(fun())
