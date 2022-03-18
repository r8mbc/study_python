# https://www.hackerrank.com/challenges/collections-counter/problem?isFullScreen=true
from collections import Counter

x = int(input())
N = Counter(map(int, input().split()))
c = int(input())

sales = 0

for i in range(c):
    size, price = map(int, input().split())
    if N[size]:
        sales += price
        N[size] -= 1

print(sales)
