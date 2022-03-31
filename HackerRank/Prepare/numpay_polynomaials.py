# https://www.hackerrank.com/challenges/np-polynomials/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

import numpy

def arrays(arr):
    A = numpy.array(arr, float)
    return A[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)