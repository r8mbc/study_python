#!/usr/bin/env python3

from collections import deque

n = int(input())
use, use2 = 0, 0
now = deque()
count = 0

if n % 2 == 1:
    print("")
else:
    for _ in range(2):
        count += 1
        q1 = list(map(int, input().split()))[1:]
        q2 = list(map(int, input().split()))[1:]

        ans = 0
        if now:
            for i in range(q2[0]):
                ans += now.popleft()
                use2 += 1
                if not now:
                    use = q2[0] - use2
                    ans += q1[0] * (q2[0] - use2)
                    break
        else:
            use = q2[0]
            ans = q1[0] * q2[0]

        for i in range(q1[1] - use - use2):
            now.append(q1[0])

        print(ans)
        if count == n // 2:
            exit()
