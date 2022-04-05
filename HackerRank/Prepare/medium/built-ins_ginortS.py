# https://www.hackerrank.com/challenges/ginorts/problem?isFullScreen=true&h_r=next-challenge&h_v=zen

S = input()

L, U, E, O = [], [], [], []

for i in range(len(S)):
    if S[i].isalpha():
        if S[i].islower():
            L.append(S[i])
        elif S[i].isupper():
            U.append(S[i])
    else:
        if int(S[i]) % 2 == 0:
            E.append(int(S[i]))
        else:
            O.append(int(S[i]))

L = sorted(L)
U = sorted(U)
O = sorted(O)
E = sorted(E)

print(*L, *U, *O, *E, sep="")
