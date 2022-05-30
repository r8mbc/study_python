#!/usr/bin/env python3

import heapq
from collections import defaultdict

q = int(input())

S = []  # 小さい
S_ = []  # 大きい

items = defaultdict(int)

for _ in range(q):
    act = list(map(int, input().split()))

    if act[0] == 1:
        heapq.heappush(S, act[1])
        heapq.heappush(S_, -act[1])
        items[act[1]] += 1
        items[-act[1]] += 1

    elif act[0] == 2:
        if items[act[1]] >= act[2]:
            items[act[1]] -= act[2]
            items[-act[1]] -= act[2]
        else:
            items[act[1]] = 0
            items[-act[1]] = 0

    else:
        while items[S[0]] == 0:
            heapq.heappop(S)
        while items[S_[0]] == 0:
            heapq.heappop(S_)
        print(-S_[0] - S[0])
