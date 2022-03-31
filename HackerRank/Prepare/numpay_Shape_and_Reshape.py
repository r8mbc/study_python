# https://www.hackerrank.com/challenges/np-shape-reshape/problem?isFullScreen=true

import numpy

N = list(map(int, input().split()))

print(numpy.reshape(N, (3, 3)))
