string = input().split(" ")
number = []
zp = 200
premia = 200
print(string)
index_meneger = 0
for i in string:
    volume = int(i)
    max_volume = max()
    premia = max(premia, volume)
    print("premia", premia)
    if max_volume >= volume:
        zp += premia
        if 0 < volume < 500:
        zp *=1.03
        elif 500 <= volume <= 1000:
        zp *= 1,05
    elif volume > 1000:
    zp *= 1.08
    print(zp)
    number.append(zp)
    print(number)
else:
    fo j in string:
    print("макс объем", max_volume, "j", int(j))

    if max_volume == int(j):

        print("нашли индекс менеджера")
    number[number.index(number)] += premia

