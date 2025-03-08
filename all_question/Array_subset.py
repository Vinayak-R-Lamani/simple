a= [11, 7, 1, 13, 21, 3, 7, 3]
b = [11, 3, 7, 1, 7]

from collections import Counter

a_count = Counter(a)
b_count = Counter(b)
ans = True
for i in b:
    if b_count[i] > a_count.get(i , 0):
        ans = False
print(a_count)
print        
print(ans)
        