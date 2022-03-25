# https://www.hackerrank.com/challenges/find-angle/problem?isFullScreen=true

import math

ab = int(input())
bc = int(input())

hy = math.hypot(ab, bc)
acos = math.degrees(math.acos(bc / hy))

degree = chr(176)

print(f"{acos:.0f}{degree}")
