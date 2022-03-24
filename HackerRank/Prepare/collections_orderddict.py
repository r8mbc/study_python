# https://www.hackerrank.com/challenges/py-collections-ordereddict/problem?isFullScreen=true
from collections import OrderedDict

zaiko = OrderedDict()

for _ in range(int(input())):
    a, b, c = input().rpartition(" ")
    zaiko[a] = zaiko.get(a, 0) + int(c)

for a, c in zaiko.items():
    print(a, c)
