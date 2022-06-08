#!/usr/bin/env python3

n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))
A.append(l)
B = [A[0]]

for i in range(n):
    B.append(A[i + 1] - A[i])


def solve(middle):
    times = 0
    piece = 0

    for i in B:
        piece += i
        if piece >= middle:
            piece = 0
            times += 1
    return times


ng = l
ok = 0

while ng - ok > 1:

    mid = (ok + ng) // 2

    if solve(mid) >= k + 1:
        ok = mid
    else:
        ng = mid

print(ok)
