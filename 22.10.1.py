import time

string = input().split(" ")
numbers = []
start_time = time.time()
print(start_time)
for i in range(int(string[0]), int(string[1])):
    count = 0
    j = 1
    while j <= i:
        if i % j == 0:
            count += 1
        j += 1
    if count == 2:
        numbers.append(i)
print("простые числа:", numbers)