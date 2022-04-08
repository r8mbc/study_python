# https://www.hackerrank.com/challenges/maximize-it/problem?isFullScreen=true

from itertools import product

K, M = map(int, input().split())

N = (list(map(int, input().split()))[1:] for _ in range(K))

result = []

for i in product(*N):
    sum = 0
    for a in i:
        sum += a**2
    result.append(sum % M)

print(max(result))
