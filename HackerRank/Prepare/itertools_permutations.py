# https://www.hackerrank.com/challenges/itertools-permutations/problem?isFullScreen=true
from itertools import permutations

string, n = input().split()
string = list(permutations(string, int(n)))

for i in string:
    print(''.join(i))