arr = [-5, -2, 5, 2, 4, 7, 1, 8, 0, -8]

negative = []
positive = []

for i in arr:
    if i < 0:
        negative.append(i)
    else:
        positive.append(i)
        
        
i , j , k  = 0 , 0 , 0
m , n = len(positive)  , len(negative)

while i < m and j < n:
    if k < len(arr):
        arr[k] = positive[i]
        i +=1
        k += 1
    if k < len(arr):
        arr[k] = negative[j]
        j +=1
        k += 1
    
while i < m:
    arr[k] = positive[i]
    i +=1
    k +=1 
    
while j < n:
    arr[k] = negative[j]
    j += 1
    k += 1
print(arr)