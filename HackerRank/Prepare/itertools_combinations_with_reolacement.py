# https://www.hackerrank.com/challenges/itertools-combinations-with-replacement/problem?isFullScreen=true
from itertools import combinations_with_replacement

string, n = input().split()
string = list(combinations_with_replacement(sorted(string), int(n)))

for i in string:
    print("".join(i))
