# https://www.hackerrank.com/challenges/np-linear-algebra/problem?isFullScreen=true
import numpy


N = [input().split() for _ in range(int(input()))]

array = numpy.array(N, float)

print(numpy.around(numpy.linalg.det(array), 2))
