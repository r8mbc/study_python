n, k = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))


def func():
    x = A[0]
    y = B[0]

    for i in range(1, len(A)):
        if abs(A[i - 1] - A[i]) <= k or abs(B[i - 1] - A[i]) <= k:
            x = A[i]
        else:
            A[i] = -999999999999999999999999
        if abs(A[i - 1] - B[i]) <= k or abs(B[i - 1] - B[i]) <= k:
            y = B[i]
        else:
            B[i] = -999999999999999999999999

        if y == B[i] or x == A[i]:
            continue
        else:
            return "No"

    if x == A[-1] or y == B[-1]:
        return "Yes"
    else:
        return "No"


print(func())
