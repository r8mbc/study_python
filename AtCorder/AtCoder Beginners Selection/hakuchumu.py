# https://atcoder.jp/contests/abs/tasks/arc065_a

s = str(input())
T = ["dream", "dreamer", "erase", "eraser"]

s = s.replace(T[-1], "").replace(T[-2], "").replace(T[-3], "").replace(T[-4], "")

if not s:
    print("YES")
else:
    print("NO")
