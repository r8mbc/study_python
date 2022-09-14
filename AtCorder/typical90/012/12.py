#!/usr/bin/env python3

from collections import defaultdict


class UnionFind:
    def __init__(self, n):
        self.n = n
        self.parents = [-1] * n

    def union(self, x, y):
        x = self.find(x)
        y = self.find(y)

        if x == y:
            return

        if self.parents[x] > self.parents[y]:
            x, y = y, x

        self.parents[x] += self.parents[y]
        self.parents[y] = x

    def same(self, x, y):
        return self.find(x) == self.find(y)


h, w = map(int, input().split())

is_red = [0] * (h * w)
uf = UnionFind(h * w)


def check(n, x):
    if is_red[x] == 1 and is_red[n] == 1:
        uf.union(n, x)
    return


q = int(input())

for i in range(q):
    A = map(int, input().split())
    if A[0] == 1:
        r, c = A[1:]
        r -= 1
        c -= 1
        is_red[r * w + c] = 1

    else:
        ra, ca, rb, cb = A[1:]
        ra -= 1
        ca -= 1
        rb -= 1
        cb -= 1
