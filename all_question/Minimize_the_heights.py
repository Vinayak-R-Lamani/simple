arr = [3, 9, 12, 16, 20]
k = 3
n = len(arr)
for i in range(n):
    if (arr[i] - k ) != 0 and  (arr[i] - k ) > 1  :
        arr[i] = arr[i] + k
        
    else:
        arr[i] = arr[i] - k
        
print(arr)
    