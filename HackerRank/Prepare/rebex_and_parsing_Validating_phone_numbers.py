# https://www.hackerrank.com/challenges/validating-the-phone-number/problem?isFullScreen=true
import re

n = int(input())

for _ in range(n):
    if re.match(r"[789]\d{9}$", input()):
        print("YES")
    else:
        print("NO")
