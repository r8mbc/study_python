# import random

s = list(input().split())
t = list(input().split())
c = 0

for i in 0, 1, 2:

    if s[i] == t[i]:
        c += 1

if c == 1:
    print("No")
else:
    print("Yes")
