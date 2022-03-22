# https://www.hackerrank.com/challenges/py-set-mutations/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

m = input()
N = set(map(int, input().split()))

for i in range(int(input())):
    a, b = input().split()
    T = set(map(int, input().split()))
    if a == "intersection_update":
        N.intersection_update(T)
    elif a == "update":
        N.update(T)
    elif a == "symmetric_difference_update":
        N.symmetric_difference_update(T)
    elif a == "difference_update":
        N.difference_update(T)

print(sum(N))
