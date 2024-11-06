s1 = input().split(" ")
s2 = input().split(" ")
num = []
num1 = []
num2 = []
s = s1 + s2
for i in s1:
    for j in s2:
        if i == j:
            num.append(int(i))
print(list(set(num)))

