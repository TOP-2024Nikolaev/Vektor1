s = input().lower().replace(" ", "" )
print(s)


r = s[::-1]
if s == r:
    print("Сьрокаюю Э" )
else:
    print("нет")
