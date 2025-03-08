string = 'AABBAA'
dict = {}

for i in string:
    dict[i] = dict.get(i , 0) + 1
for i in dict:
    dict[i] += 2
print(dict)