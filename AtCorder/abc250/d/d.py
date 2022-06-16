#!/usr/bin/env python3

n = int(input())
s = range(1, n + 1)


def enum_primes(n):
    prime_flag = [1] * (n + 1)
    prime_flag[0] = 0
    prime_flag[1] = 0

    i = 2
    while i * i <= n:
        if prime_flag[i]:
            for j in range(2 * i, n + 1, i):
                prime_flag[j] = 0
        i += 1
    return [i for i in range(n + 1) if prime_flag[i]]


sosu = enum_primes(10**6 + 5)

count = 0
for i in range(len(sosu)):
    sanjo = sosu[i] ** 3
    for j in range(i):
        if sanjo * sosu[j] > n:
            break
        count += 1


print(count)
