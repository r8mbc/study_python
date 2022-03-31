# https://www.hackerrank.com/challenges/np-mean-var-and-std/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen
import numpy


a, b = input().split()
N = [input().split() for _ in range(int(a))]

array = numpy.array(N, int)

print(numpy.mean(array, axis=1))
print(numpy.var(array, axis=0))
print(numpy.around(numpy.std(array), 11))
