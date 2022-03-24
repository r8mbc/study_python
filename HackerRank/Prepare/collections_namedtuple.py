# https://www.hackerrank.com/challenges/py-collections-namedtuple/problem?isFullScreen=true
from collections import namedtuple

n = int(input())
a = input().split()

student = namedtuple("student", a)
points = 0

for _ in range(n):
    b, c, d, e = input().split()
    f = student(b, c, d, e)
    points += int(f.MARKS)

print(f"{points / n:.2f}")
