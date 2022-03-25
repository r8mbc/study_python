# https://www.hackerrank.com/challenges/compress-the-string/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

from itertools import groupby

gr = groupby(input())
ans = []

for key, group in gr:
    ans.append((len(list(group)), int(key)))

print(*ans)
