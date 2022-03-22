# https://www.hackerrank.com/challenges/py-set-discard-remove-pop/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen


n = int(input())
s = set(map(int, input().split()))

for i in range(int(input())):
    a = input().split()
    if a[0] == "remove":
        s.remove(int(a[1]))
    elif a[0] == "discard":
        s.discard(int(a[1]))
    else:
        s.pop()

print(sum(s))
