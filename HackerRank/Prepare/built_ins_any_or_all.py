# https://www.hackerrank.com/challenges/input/problem?isFullScreen=true

x = int(input())
N = list(input().split())

print(all([int(i) > 0 for i in N]) and any([j == j[::-1] for j in N]))
