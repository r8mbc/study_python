n, x = map(int, input().split())
s = input()


1 2 4 8 16
1 3 7 15 



# 層
start = 0
for i in range(len(s)):
    if s[i] == "U":
        start -= 1
    else:
        start += 1


