# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
from itertools import combinations

string, n = input().split()
a = []

for i in range(1, int(n) + 1):
    a.extend(list(combinations(sorted(string), i)))


for i in a:
    print("".join(i))
