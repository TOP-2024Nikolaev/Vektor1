
a1 = 10
b1 = 20
matrix=[[1,2,3],[4,5,6],[7,8,9],[a1,[13,14,[15,16,"ok"]],b1]]
search = "ok"
for i in matrix:
    print("уровень первый", i)
    for j in i:
        print("уроввень второй", j)
    if j == search:
    print("нашли ОК","  ")
    break

