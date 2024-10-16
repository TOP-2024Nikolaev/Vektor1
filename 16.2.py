k = 0
count_max = 0
for i in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(i):
        count_max +=1
        print("Количество максимальныъ значаний:", count_max)
        number[k] += premia / count_max      

k += 1
