# https://www.hackerrank.com/challenges/re-start-re-end/problem?isFullScreen=true

import re

a = input()
b = input()

pattern = re.compile(b)
m = pattern.search(a)
if not m:
    print("(-1, -1)")
while m:
    print("({0}, {1})".format(m.start(), m.end() - 1))
    m = pattern.search(a, m.start() + 1)
