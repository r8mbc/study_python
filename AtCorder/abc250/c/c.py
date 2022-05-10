#!/usr/bin/env python3


def solve():
    n, q = map(int, input().split())

    X = list(int(input()) for _ in range(q))

    a = list(range(1, n + 1))

    for i in range(len(X)):
        for k in range(i + 1, len(X)):
            if (X[i] + 1) == X[k]:
                X.remove(X[i])
                X.remove(X[k])
            elif X[i] == X[k]:
                break

    print(X)

    for i in X:
        b = a.index(i)

        if b + 1 == n:
            a[b], a[b - 1] = a[b - 1], a[b]
        else:
            a[b], a[b + 1] = a[b + 1], a[b]

    return a


print(*solve())
