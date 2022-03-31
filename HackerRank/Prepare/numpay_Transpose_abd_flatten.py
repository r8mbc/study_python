# https://www.hackerrank.com/challenges/np-transpose-and-flatten/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

import numpy

n, m = input().split()
li = [list(map(int, input().split())) for _ in range(int(n))]

array = numpy.array(li)

print(numpy.transpose(array))
print(array.flatten())
