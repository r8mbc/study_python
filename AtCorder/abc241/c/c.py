#!/usr/bin/env python3


def solve():

    n = int(input())
    S = [input() for _ in range(n)]

    def count(a, b, next_a, next_b):
        count = 0

        for _ in range(6):
            if not (0 <= a < n and 0 <= b < n):
                return False
            if S[a][b] == "#":
                count += 1
            a += next_a
            b += next_b
        return count >= 4

    next_as = [1, 0, 1, 1]
    next_bs = [0, 1, 1, -1]

    for i in range(n):
        for j in range(n):
            for next_a, next_b in zip(next_as, next_bs):
                if count(i, j, next_a, next_b):
                    return "Yes"

    return "No"


print(solve())
