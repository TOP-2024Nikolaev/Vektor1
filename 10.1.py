customers=['Bob','Anna','Joe','Bill','Nick']
result=""
for i in customers:
    result += i + "-"
print(result.split("-")[:-1])