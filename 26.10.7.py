s1 = input().split(" ")
s2 = input().split(" ")
num = []
num1 = max([int(s) for s in s1]), min([int(s) for s in s1])
num2 = max([int(s) for s in s2]), min([int(s) for s in s2])


print(list(num1))
print(list(num2))