N = int(input())
A = list(set(map(int, input().split())))

for i in range(len(A)):
    if A[i] != i:
        print(i)
        break
    if A[-1] == i:
        print(len(A))
