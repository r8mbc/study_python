# https://www.hackerrank.com/challenges/word-order/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from collections import Counter

n = [input() for _ in range(int(input()))]
c = Counter(n)

print(len(c))
print(*c.values())
