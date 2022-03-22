# https://www.hackerrank.com/challenges/py-introduction-to-sets/problem?isFullScreen=true


def average(array):
    # your code goes here
    N = set(array)
    return f"{sum(N) / len(N):.3f}"


if __name__ == "__main__":
    n = int(input())
    arr = list(map(int, input().split()))
    result = average(arr)
    print(result)
