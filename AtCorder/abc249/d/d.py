#!/usr/bin/env python3

n = int(input())
A = sorted(list(map(int, input().split())))

count = dict()

for i in range(n):
    if A[i] in count:
        count[A[i]] += 1
    else:
        count[A[i]] = 1

ans = 0
print(count)

if min(A) == 1:
    for value in count.values():
        if value >= 2:
            ans += value - 1

for key,value in count.items():
    a = key + __
    if a in count:
        ans += count[a]

print(ans)
