n, k, x = map(int, input().split())
A = map(int, input().split())

harau = []
tsukau = []

for i in A:
    tsukau.append(i // x)
    harau.append(i % x)

if sum(tsukau) < k:
    amari = k - sum(tsukau)
    harau.sort(reverse=True)
    if amari > len(harau):
        print(0)
    else:
        harau = harau[amari:]
        print(sum(harau))

elif sum(tsukau) == k:
    print(sum(harau))

else:
    tarinai = sum(tsukau) - k
    tarinai_okane = tarinai * x
    print(sum(harau) + tarinai_okane)
