# https://www.hackerrank.com/challenges/symmetric-difference/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

m = input()
a = set(map(int, input().split()))
n = input()
b = set(map(int, input().split()))

c = a.difference(b)
c = c.union(b.difference(a))

print(*sorted(c), sep="\n")
