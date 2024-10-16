string = input().split(" ")



base = 200
percent = 0
premiya = 200
zp = int('i')
print('zp_all')

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

k = 0

for i in string:
    zp = int(i)
    if 0 < zp < 500:
        percent = 0.03
    elif 500 <= zp < 1000:
        percent = 0.05
    elif zp >= 1000:
        percent = 0.08

    if
    print("Менеджер №1:" , base *(1 + percent) + premiya)
