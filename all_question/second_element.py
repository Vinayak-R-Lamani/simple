# arr = [1,2,3]
arr = [2,4,1,3,5]

n = len(arr)
ind = -1

for i in range(n - 2 , - 1, -1):
    if arr[i] < arr[i + 1]:
        ind = i
        break
    
if ind == -1:
    arr.reverse()
    
for i in range(n -1 , ind , -1):
    if arr[i] > arr[ind]:
        arr[i] , arr[ind] = arr[ind] , arr[i]
        break
    
arr[ind + 1:] = reversed(arr[ind +1:])
print(arr)