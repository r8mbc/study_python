# https://atcoder.jp/contests/abs/tasks/arc089_a

n = int(input())
S = [input().split() for _ in range(n)]

for i in range(n):
    if i > 0:
        time = int(S[i][0]) - int(S[i - 1][0])
        x = int(S[i][1]) - int(S[i - 1][1])
        y = int(S[i][2]) - int(S[i - 1][2])
    else:
        time = int(S[i][0])
        x = int(S[i][1])
        y = int(S[i][2])

    step = abs(x + y)

    if step > time:
        print("No")
        break
    elif (step == 0 and time % 2 == 0) or (step % 2 == time % 2):
        if i == n - 1:
            print("Yes")
            break
    else:
        print("No")
        break
