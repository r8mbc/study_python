#!/usr/bin/env python3

a, b, c, d, e, f, x = map(int, input().split())

ta = x // (a + c)
if x % (a + c) >= a:
    ta_amari = a
else:
    ta_amari = x % (a + c)

ao = x // (d + f)
if x % (d + f) > d:
    ao_amari = d
else:
    ao_amari = x % (d + f)

if (ta * a + ta_amari) * b > (ao * d + ao_amari) * e:
    print("Takahashi")
elif (ta * a + ta_amari) * b < (ao * d + ao_amari) * e:
    print("Aoki")
else:
    print("Draw")
