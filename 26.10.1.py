c = []
for i in range(100, 1000):
    s = str(i)
    a = []
    for j in str(s):
            a.append(j)
        if a[0]==a[1] or a[1]==a[2] or a[0]==a[2]:
            if a[0] !=a[1] != a[2]:
            b.append(int(a[0]+a[1]+a[2]))
print(len(c))
