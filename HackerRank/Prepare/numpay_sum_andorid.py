# https://www.hackerrank.com/challenges/np-sum-and-prod/problem?isFullScreen=true

import numpy

numpy.set_printoptions(legacy="1.13")

a, b = input().split()
N = [input().split() for _ in range(int(a))]


array = numpy.array(N, int)
sum = numpy.sum(array, axis=0)
print(numpy.prod(sum, axis=0))
