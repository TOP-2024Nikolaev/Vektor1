s = input().split(" ")
res = []
for i in range(int(s[0]),int(s[1])):
    e = str(i)
    numbers = []
    for j in e:
        numbers.append(j)
    count = 0
    for x in numbers:
        if numbers[0] == x:
            count+= 1
        if count == 2:
            res.append(i)
print(res)

