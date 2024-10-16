



status = 0
if (int(string[0]) > int(string[1])
    or int(string[0]) > int(string[2])):
status = 0
elif (int(string[1]) > int(string[2])
    or int(string[1]) > int(string[0])):
status = 1
elif (int(string[2]) > int(string[1])
    or int(string[2]) > int(string[0])):
status = 2
print(status)