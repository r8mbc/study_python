n = int(input())
A = sorted(list(map(int, input().split())))

sunuke = []
saisho = []

k = 0
ans = []

for c in range(n):
    C = A
    B = A[(n - c) :] + A[: (n - c)]
    k = 0

    for i in range(n // 2):
        sunuke.append(C[c])
        del C[c]
        saisho.append(C[0])
        del C[0]
    for b in sunuke:
        k += B.index(b)
        ans.append(k)

print(ans)

print(max(ans), ans.index(max(ans)))
