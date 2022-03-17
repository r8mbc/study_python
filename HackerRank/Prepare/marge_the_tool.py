# https://www.hackerrank.com/challenges/merge-the-tools/problem?isFullScreen=true

def merge_the_tools(s, k):
    # your code goes here
    i = 0
    a = []
    while i <= len(s) - k:
        st = []
        for j in range(k):
            st.append(s[i + j])
        st = sorted(set(st), key=st.index)
        a.append(st)
        i += k

    for i in a:
        print(*i, sep="")


if __name__ == "__main__":
    string, k = input(), int(input())
    merge_the_tools(string, k)
