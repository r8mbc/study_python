# https://www.hackerrank.com/challenges/np-min-and-max/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

numpy.set_printoptions(legacy="1.13")

a, b = input().split()
N = [input().split() for _ in range(int(a))]


array = numpy.array(N, int)
min = numpy.min(array, axis=1)
print(numpy.max(min))
