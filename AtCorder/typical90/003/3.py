#!/usr/bin/env python3

n = int(input())

A = [[] for _ in range(n)]

for i in range(n - 1):
    x, y = map(int, input().split())
    x, y = x - 1, y - 1
    A[y].append(x)
    A[x].append(y)


def dists(s):
    dist = [-1] * n
    dist[s] = 0

    st = [s]

    while st:
        v = st.pop()
        for nv in A[v]:
            if dist[nv] == -1:
                st.append(nv)
                dist[nv] = dist[v] + 1

    return dist


dist0 = dists(0)
index = dist0.index(max(dist0))
r_dist = dists(index)

print(max(r_dist) + 1)
