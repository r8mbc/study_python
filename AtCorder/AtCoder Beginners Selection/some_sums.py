# https://atcoder.jp/contests/abs/tasks/abc083_b

n, a, b = map(int, input().split())

add = 0

for i in range(n+1):
    num = 0
    for j in str(i):
        num += int(j)
    if a <= num <= b:
        add += i

print(add)
