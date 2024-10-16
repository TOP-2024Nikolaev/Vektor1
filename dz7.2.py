string = input().split(" ")

begin = int(string[0])
end = int(string[1])
result = ""
for i in range(begin, end +1):
    j = end + 1
    result += str(i) + " "
    print(i)