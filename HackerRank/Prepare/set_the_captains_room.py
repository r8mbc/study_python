# https://www.hackerrank.com/challenges/py-the-captains-room/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

k = int(input())
rooms = list(map(int, input().split()))

ans = (sum(set(rooms)) * k - sum(rooms)) / (k - 1)
print(f"{ans:0.0f}")
