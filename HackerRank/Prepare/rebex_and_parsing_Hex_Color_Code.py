# https://www.hackerrank.com/challenges/hex-color-code/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import re

n = int(input())

for _ in range(n):
    a = input().split()

    if len(a) > 1 and "{" not in a:
        x = re.findall(r"#[a-fA-F0-9]{3,6}", str(a))
        [print(i) for i in x]
