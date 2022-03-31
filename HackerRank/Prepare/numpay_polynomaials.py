# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

A = numpy.array(input().split(), float)
B = int(input())


print(numpy.polyval(A, B))
