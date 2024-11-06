s = input().split(" ")
c =[]
for i in range(int(s[0]), int(s[1]) + 1):
    b = []
    for x in str(i):
        b.append(x)
    for j in range(10):
        if b.count(str(j)) == 2:
            c.append(i)
print(c)  
