n = int(input())
t = list(range(1, 2 * n + 2))

for i in range(1, len(t)):
    print(t[0], flush=True)
    t.remove(t[0])

    if not t:
        break

    a = int(input())
    if a in t:
        t.remove(a)


exit()
