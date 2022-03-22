# https://www.hackerrank.com/challenges/py-check-strict-superset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

A = set(map(int, input().split()))
n = int(input())


def func():
    for i in range(n):
        B = set(map(int, input().split()))
        if A >= B:
            continue
        else:
            return "False"
    return "True"


print(func())
