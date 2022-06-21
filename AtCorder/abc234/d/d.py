#!/usr/bin/env python3


import heapq


n, k = map(int, input().split())

P = list(map(int, input().split()))

B = sorted(P[:k])
heapq.heapify(B)

print(B[0])

P = P[k:]

for i in P:
    if i > B[0]:
        heapq.heappop(B)
        heapq.heappush(B, i)
    print(B[0])
