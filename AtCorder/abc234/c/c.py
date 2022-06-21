#!/usr/bin/env python3

k = int(input())

n = 3
a = bin(k)[2:]
ans = ""
for i in str(a):
    if i == "1":
        ans += "2"
    else:
        ans += "0"

print(ans)
