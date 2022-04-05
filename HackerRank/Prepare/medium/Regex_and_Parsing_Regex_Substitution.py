# https://www.hackerrank.com/challenges/re-sub-regex-substitution/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import re

n = int(input())


for _ in range(n):
    a = input()
    if not re.match("^#", a):
        a = re.sub(r"(?<=\s)\&{2,2}\s", "and ", a)
        print(re.sub(r"(?<=\s)\|{2,2}\s", "or ", a))
    else:
        print(a)
