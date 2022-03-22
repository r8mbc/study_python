# https://www.hackerrank.com/challenges/swap-case/problem?isFullScreen=true


def swap_case(s):
    a = ""
    for i in range(len(s)):
        if s[i].isupper():
            a += s[i].lower()
        else:
            a += s[i].upper()

    return a


if __name__ == "__main__":
    s = input()
    result = swap_case(s)
    print(result)
