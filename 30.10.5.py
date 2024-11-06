#найти наибольшее число в списке являющееся полным квадратом некоторого числаs
s = input().split(" ")
n = []
m = 0
for i in range(int(s[0]),int(s[1])):
    k = int(i ** 0.5)
    print(k)
    if i == k * k:
        n.append(i)
print(n)
