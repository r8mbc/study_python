# https://www.hackerrank.com/challenges/re-group-groups/problem?isFullScreen=true


import re

if __name__ == "__main__":
    n = input()
    m = re.findall(r"([0-9a-zA-Z])\1+", n)

if m:
    print(m[0])
else:
    print(-1)
