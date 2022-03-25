# https://www.hackerrank.com/challenges/py-collections-deque/problem?isFullScreen=true
from collections import deque

n = deque()

for _ in range(int(input())):
    a = input().split()
    if a[0] == "append":
        n.append(a[1])
    elif a[0] == "appendleft":
        n.appendleft(a[1])
    elif a[0] == "pop":
        n.pop()
    elif a[0] == "popleft":
        n.popleft()

print(*n)
