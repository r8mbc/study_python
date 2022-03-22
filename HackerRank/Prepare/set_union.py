# https://www.hackerrank.com/challenges/py-set-union/problem?isFullScreen=true

e = input()
eng = set(input().split())
f = input()
fra = set(input().split())

all = eng | fra
print(len(all))
