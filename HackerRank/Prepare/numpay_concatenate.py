# https://www.hackerrank.com/challenges/np-concatenate/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

n, m, p = map(int, input().split())

A = [input().split() for _ in range(n)]
B = [input().split() for _ in range(m)]

arrayA = numpy.array(A, int)
arrayB = numpy.array(B, int)

print(numpy.concatenate((arrayA, arrayB), axis=0))
