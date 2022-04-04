import math

N = int(input())


def func():
    if N == 0:
        return 0

    a = 1
    b = 1

    M = (N / 4) ** (1 / 3)
    print(M)

    a = math.ceil(M)
    b = math.floor(M)

    x = a**3 + a**2 * b + a * b**2 + b**3
    print(a, b)
    print(x)

    if x < N:
        b += 1
        x = a**3 + a**2 * b + a * b**2 + b**3

    print(a, b)
    return x


print(func())
