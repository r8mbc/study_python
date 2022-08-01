#!/usr/bin/env python3

n = int(input())

ST = list([0, 0] for _ in range(n))

setS = set()

for i in range(n):
    ss, tt = input().split()

    if ss not in setS:
        ST[i][0] = int(tt)
        ST[i][1] = i
        setS.add(str(ss))


most = 0
ans = 0

for i in ST:
    if most < i[0]:
        most = i[0]
        ans = i[1] + 1


print(ans)
