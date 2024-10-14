string = input("Введите стоимость, с кого звоним, куда звоним").split(" ")
price = float(string[0])
mtot = 0
mtob = 1
ttob = 2
mtom = 3
btob = 4
ttot = 5
if string[1] =="m" and string[2]=="t":
    result = price * 0.2
    print(result)