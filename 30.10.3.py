keys = (1,2,3,4,5,6,7,8)

values = ['a','b','c','d','e','f','g','h']

d1 = {}

for keys, values in zip(keys, values):
    d1[keys] = values
print(d1)


