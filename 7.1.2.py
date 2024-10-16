string = input()
print(string)
if 0 < int(string) > 100:

    print("Введенные числа вне диапозона")
else:
    number = int(string)
    print(number)
    if number % 3 == 0 and number % 5 != 0:
        print("Fizz")
    if number % 5 == 0 and number % 3 != 0:
        print("Buzz")
    if number % 15 == 0:
        print("Fizz Buzz")
else:
    print("Число: ", number)