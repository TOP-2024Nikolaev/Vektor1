string = input().split(" ")

begin = int(string[0])
end = int(string[1])

for i in range(begin, end):
    if i % 7 == 0:
        print(i)

