# https://www.hackerrank.com/challenges/zipped/problem?isFullScreen=true

n, s = map(int, input().split())
A = []
for _ in range(s):
    A.append(map(float, input().split()))

for i in zip(*A):
    print(sum(i) / len(i))
