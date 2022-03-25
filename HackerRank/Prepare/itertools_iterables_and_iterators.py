# https://www.hackerrank.com/challenges/iterables-and-iterators/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

from itertools import combinations

a = int(input())
b = input().split()
c = int(input())

len_b = len(list(combinations(b, c)))
count_a = b.count("a")
count = 0

for i in combinations(b, c):
    if "a" in i:
        count += 1

print(f"{count / len_b}")
