# https://www.hackerrank.com/challenges/py-set-intersection-operation/problem?isFullScreen=true&h_r=next-challenge&h_v=zen


e = input()
eng = set(input().split())
f = input()
fra = set(input().split())

all = eng & fra
print(len(all))
