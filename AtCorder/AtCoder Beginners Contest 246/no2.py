import math

a, b = map(int, input().split())

if a == 0:
    y = 0
    if b > 0:
        x = 1
    else:
        x = -1
elif b == 0:
    x = 0
    if a > 0:
        y = 1
    else:
        y = -1
else:
    x = math.sqrt(b**2 / (b**2 + a**2))
    y = abs(a) / abs(b) * x

if a < 0:
    y = -y
if b < 0:
    x = -x


print(y, x)
