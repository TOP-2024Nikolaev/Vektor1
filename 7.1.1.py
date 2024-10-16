string = input()
print(string)
if 0 < int(string) > 100:

    print("Введенные числа вне диапозона")
else:
    number = int(string[1])
    print(number % 3)
    if number % 3 == 0:
        print("Fizz")
