# https://www.hackerrank.com/challenges/np-eye-and-identity/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

numpy.set_printoptions(legacy="1.13")

n, m = map(int, input().split())

print(numpy.eye(n, m, k=0))
