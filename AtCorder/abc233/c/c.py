#!/usr/bin/env python3

n, x = map(int, input().split())

ans = [1]

for _ in range(n):
    count = []

    c = list(map(int, input().split()))
    d = c[1:]

    for i in ans:
        for j in d:
            if i * j <= x:
                count.append(i * j)
    ans = count

print(ans.count(x))
