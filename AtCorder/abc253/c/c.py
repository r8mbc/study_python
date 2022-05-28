#!/usr/bin/env python3

from collections import defaultdict
import sys

input = sys.stdin.readline

q = int(input())

S = defaultdict(int)

for _ in range(q):
    act = list(map(int, input().split()))

    if len(act) == 1:
        print(max(S.keys()) - min(S.keys()))

    elif len(act) == 2:
        S[act[1]] += 1

    else:
        if act[2] >= S[act[1]]:
            S.pop(act[1])
        else:
            S[act[1]] -= act[2]
