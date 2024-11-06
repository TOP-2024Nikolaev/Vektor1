import re
s = input("введите логин")
p = r'\'

st = re.findall(p, s)

print(st)
if not st:
    print("логин верный", s)

