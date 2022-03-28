# https://www.hackerrank.com/challenges/map-and-lambda-expression/problem?isFullScreen=true

cube = lambda x: pow(x, 3)  # complete the lambda function


def fibonacci(n):
    # return a list of fibonacci numbers
    if n >= 2:
        A = [0, 1]
    elif n == 1:
        return [0]
    else:
        return []
    B = []

    for i in range(2, n):
        A.append(A[i - 2] + A[i - 1])

    return A


if __name__ == "__main__":
    n = int(input())
    print(list(map(cube, fibonacci(n))))
