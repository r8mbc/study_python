# https://atcoder.jp/contests/abs/tasks/abc085_c

n, y = map(int, input().split())


def function():
    if y % 10000 % 5000 % 1000 == 0:
        for i in range(n + 1):
            for j in range(n - i + 1):
                k = n - i - j
                if 10000 * i + 5000 * j + 1000 * k == y:
                    return i, j, k
    return -1, -1, -1


print(*function())
