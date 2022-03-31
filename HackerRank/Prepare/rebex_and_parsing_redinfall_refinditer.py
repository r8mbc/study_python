# https://www.hackerrank.com/challenges/re-findall-re-finditer/problem?isFullScreen=true

import re

boin = "aiueoAIUEO"
shiin = "qwrtypsdfghjklzxcvbnmQWRTYPSDFGHJKLZXCVBNM"

find = re.findall(r"(?<=[%s])([%s]{2,})[%s]" % (shiin, boin, shiin), input())

print("\n".join(find or ["-1"]))
