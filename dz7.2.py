string = input().split(" ")
begin = int(string[0])
end = int(string[1])
result = " "
j = end
for i in range(begin, end +1):
    j -= 2
    result += str(i) + " "
print(result)