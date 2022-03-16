# https://atcoder.jp/contests/abs/tasks/abc081_b

n = input()
a = list(map(int, input().split()))

for i in range(len(a)):
    count = 0
    while a[i] % 2 == 0:
        a[i] = a[i] // 2
        count += 1
    a[i] = count

a.sort()

print(a[0])