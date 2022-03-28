n, m = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

b1 = B[-1] // A[-1]
b2 = B[-1] * A[0]
b3 = B[0] // A[0]

print(b3, b2, b1)
