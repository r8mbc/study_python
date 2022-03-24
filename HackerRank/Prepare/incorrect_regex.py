# https://www.hackerrank.com/challenges/incorrect-regex/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

for _ in range(int(input())):
    ans = True
    try:
        p = re.compile(input())
    except re.error:
        ans = False
    print(ans)
