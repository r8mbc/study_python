#!/usr/bin/env python3

aa, bb = map(str, input().split())
aa, bb = aa[::-1], bb[::-1]

ans = 0
i = 0
while ans <= 9 and i <= min(len(aa) - 1, len(bb) - 1):
    ans = int(aa[i]) + int(bb[i])
    i += 1

if ans <= 9:
    print("Easy")
else:
    print("Hard")
