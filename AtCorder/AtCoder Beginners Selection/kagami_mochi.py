# https://atcoder.jp/contests/abs/tasks/abc085_b

n = int(input())
D = set([input() for _ in range(n)])

count = 0

for i in D:
    if i != 0:
        count += 1
    else:
        break

print(count)
