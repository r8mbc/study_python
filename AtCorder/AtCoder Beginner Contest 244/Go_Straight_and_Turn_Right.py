n = int(input())
t = str(input())

x, y = 0, 0

t = t.split("R")

for i in range(len(t)):
    if i == 0 or i % 4 == 0:
        x += len(t[i])
    elif i % 4 == 1:
        y -= len(t[i])
    elif i % 4 == 2:
        x -= len(t[i])
    elif i % 4 == 3:
        y += len(t[i])

print(x, y)
