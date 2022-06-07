#!/usr/bin/env python3

n = int(input())


def prime_factorize(n):
    a = []
    while n % 2 == 0:
        a.append(2)
        n //= 2
    f = 3
    while f * f <= n:
        if n % f == 0:
            a.append(f)
            n //= f
        else:
            f += 2
    if n != 1:
        a.append(n)
    return a


ans = prime_factorize(n)

if len(ans) == 1:
    print(0)
else:
    i = 0
    while True:
        if len(ans) <= 2**i:
            break
        i += 1

    print(i)
