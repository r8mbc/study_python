# https://atcoder.jp/contests/typical90/tasks/typical90_a

n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))
B = [A[0], l - A[-1]]

for i in range(1, n):
    B.insert(i, A[i] - A[i - 1])


def func():
    mini = l // (k + 1)
    for i in range(mini, 0, -1):
        count = 0
        length = 0
        for j in range(n + 1):
            length += B[j]
            if j == n and count == k:
                if length < i:
                    break
                else:
                    return i
            elif length >= i:
                length = 0
                count += 1


print(func())
