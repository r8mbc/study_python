# https://atcoder.jp/contests/typical90/tasks/typical90_a

n, l = map(int, input().split())
k = int(input())
A = list(map(int, input().split()))
B = [A[0], l - A[n - 1]]

for i in range(1, n):
    B.insert(i, A[i] - A[i - 1])

mini = l // (k + 1)
peaces = []
a = 0

def func():
    for i in range(mini, 0, -1):
        for j in range(n):
            if sum(B[a:j]) >= i:

# こんがらがってきたので一時休戦

print(func())
