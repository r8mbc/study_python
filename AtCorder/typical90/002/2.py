n = int(input())

if n % 2 != 0:
    print("")
    exit()


def solve(word):
    line = 0
    moji = ""

    for j in str(word):
        if j == "0":
            line += 1
            moji += "("
        else:
            line -= 1
            moji += ")"

        if line < 0:
            return False
    if line == 0:
        return moji


for i in range(2**n):
    b = bin(i)[2:].zfill(n)

    ans = solve(b)
    if ans:
        print(ans)
