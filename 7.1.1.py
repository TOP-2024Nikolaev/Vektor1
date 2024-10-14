string = input()
if (0 < int(string[0]) > 100 or  0 < int(string[1]) > 100):

    print("Введенные числа вне диапозона")
else:
    number = int(string[0])
    if number % 3 == 0:
        print("Fizz")
