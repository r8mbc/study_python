# https://atcoder.jp/contests/abs/tasks/abc088_b

n = input()
a = sorted(map(int, input().split()), reverse=True)
alice, bob, i = 0, 0, 0

while i <= len(a) - 1:
    alice += a[i]
    if i + 1 <= len(a) - 1:
        bob += a[i + 1]
    i += 2

print(alice - bob)
