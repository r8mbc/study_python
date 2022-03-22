# https://www.hackerrank.com/challenges/no-idea/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

n, m = input().split()
S = list(map(int, input().split()))
A = set(map(int, input().split()))
B = set(map(int, input().split()))

C = A | B

count = 0

for i in S:
    if i in A:
        count += 1
    if i in B:
        count -= 1

print(count)
