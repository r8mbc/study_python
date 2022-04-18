n, x = map(int, input().split())
s = input()


# 無意味な移動を消す
A = []

for i in s:
    if i == "U" and len(A) > 0 and A[-1] != "U":
        A.pop()
    else:
        A.append(i)

for i in A:
    if i == "U":
        x = x // 2
    elif i == "R":
        x = x * 2 + 1
    else:
        x *= 2

print(x)
