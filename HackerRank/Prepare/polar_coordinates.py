# https://www.hackerrank.com/challenges/polar-coordinates/problem?isFullScreen=true
import cmath


a = complex(input())
a = complex(a.real, a.imag)

print(abs(a))
print(cmath.phase(a))
