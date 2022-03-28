# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

import re

for _ in range(int(input())):
    print(bool(re.match(r"^[-+]?[0-9]*\.[0-9]+$", input())))
