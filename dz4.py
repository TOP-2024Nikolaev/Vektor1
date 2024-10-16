string = input()
result = ""
for number in range(begin, end + 1):
    if number % 3 == 0 and number % 5 != 0:
        result += "Fizz" + str(number) + ", "
    if number % 5 ==0 and number % 3 !=0:
        result +- "Buzz:" + str(number) + ", "
    if number % 15 == 0:
        result +- "Fizz Buzz:" + str(number) + ", "
    else:
        result +="Число:" + str(number) + ","
print(result)