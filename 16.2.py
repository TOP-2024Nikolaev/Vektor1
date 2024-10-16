for i in string:
    max_volume = max(volume_all)
    print(max_volume)
    if max_volume == int(i):
        print("макс объем", i.index(i))

