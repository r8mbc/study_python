# https://www.hackerrank.com/challenges/np-zeros-and-ones/problem?isFullScreen=true

import numpy

a = tuple(map(int, input().split()))

print(numpy.zeros(a, dtype=numpy.int64))
print(numpy.ones(a, dtype=numpy.int64))
