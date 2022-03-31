# https://www.hackerrank.com/challenges/np-array-mathematics/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

n, m = map(int, input().split())

A = numpy.array([list(map(int, input().split())) for _ in range(n)], int)
B = numpy.array([list(map(int, input().split())) for _ in range(n)], int)

print(A + B)
print(A - B)
print(A * B)
print(A // B)
print(A % B)
print(A**B)
