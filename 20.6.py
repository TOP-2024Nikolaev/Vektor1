string = input().split('')
even = 0
even_numbers = []
odds = 0
odds_numbers = []
int9 = 0
int9_numbers = []
for i in range(int(string[0]), int(string[1])):
    if i % 2 ==0:
        even += 1
        even_numbers.append(i)
    if i % 2 !=0:
        odds += 1
        odds_numbers.append(i)
    if i % 9 == 0:
        int9 += 1
        int_numbers.append(i)
print("Количество четных:", even, "ср.арифмет.")
