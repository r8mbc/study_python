# https://www.hackerrank.com/challenges/py-check-subset/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n = int(input())

for i in range(n):
    p = input()
    A = set(map(int, input().split()))
    q = input()
    B = set(map(int, input().split()))
    if A <= B:
        print("True")
    else:
        print("False")
