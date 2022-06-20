#!/usr/bin/env python3

n = int(input())
A = list(map(int, input().split()))

count = 0
top = [[0, 0]]

for i in range(n):
    count += 1

    t_number, t_count = top[-1]
    if A[i] == t_number:
        top[-1][1] += 1
    else:
        top.append([A[i], 1])

    if top[-1][0] == top[-1][1]:
        top.pop()
        count -= A[i]
    print(count)
