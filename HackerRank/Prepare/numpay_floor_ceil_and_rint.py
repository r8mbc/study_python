# https://www.hackerrank.com/challenges/floor-ceil-and-rint/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

numpy.set_printoptions(legacy="1.13")

N = input().split()

array = numpy.array(N, float)

print(numpy.floor(array))
print(numpy.ceil(array))
print(numpy.rint(array))
