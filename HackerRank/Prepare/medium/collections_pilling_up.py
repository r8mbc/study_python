# https://www.hackerrank.com/challenges/piling-up/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from collections import deque

t = int(input())

for _ in range(t):
    a = int(input())
    B = deque(map(int, input().split()))
    if B[0] == B[-1]:
        c = B.pop()
        B.popleft()
    else:
        if B[0] > B[-1]:
            c = B.popleft()
        else:
            c = B.pop()

    while len(B) >= 1:
        if len(B) == 1:
            print("Yes")
            break
        if c < B[0] or c < B[-1]:
            print("No")
            break
        else:
            if B[0] >= B[-1]:
                c = B.popleft()
            else:
                c = B.pop()
