# https://www.hackerrank.com/challenges/validating-named-email-addresses/problem?isFullScreen=true&h_r=next-challenge&h_v=zen
import re

n = int(input())

for _ in range(n):
    a, b = input().split()
    if re.match(r"<[A-Za-z](\w|-|\.|_)+@[A-Za-z]+\.[A-Za-z]{1,3}>", b):
        print(a, b)
