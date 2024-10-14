string = input().splint(" ")
numbers =[]
for i in string:
    numbers.append(int(i))
    numbers.sort()
    print(numbers)
