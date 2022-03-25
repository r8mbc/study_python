# https://www.hackerrank.com/challenges/defaultdict-tutorial/problem?isFullScreen=true

from collections import defaultdict

n, m = map(int, input().split())
A = [input() for _ in range(n)]

d = defaultdict(list)


for i in range(1, n + 1):
    d[A[i - 1]].append(str(i))

for i in range(m):
    b = input()
    if b in d:
        print(" ".join(d[b]))
    else:
        print(-1)
