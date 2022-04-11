#!/usr/bin/env python3

from collections import deque

n = int(input())
now = deque()
count = 0

if n >= 1 and n % 2 == 1:
    print("")
    exit()

for _ in range(n // 2):
    q1 = list(map(int, input().split()))
    q2 = list(map(int, input().split()))

    if len(q1) != 3 or len(q2) != 2 or q1[0] != 1 or q2[0] != 2:
        print("")
        exit()

    q1 = q1[1:]
    q2 = q2[1:]

    now.append([q1[0], q1[1]])
    ans = 0

    if now[0][1] >= q2[0]:
        ans += now[0][0] * q2[0]
        now[0][1] -= q2[0]
    else:
        toru = q2[0]
        for i in range(len(now)):
            if toru >= now[i][1]:
                ans += now[i][0] * now[i][1]
                toru -= now[i][1]
                now[i][1] = 0
            else:
                ans += now[i][0] * toru
                now[i][1] -= toru
                toru = 0
                break

    for i in range(len(now)):
        if now[0][1] == 0:
            now.popleft()
        else:
            break
    print(now)
    print(ans)
