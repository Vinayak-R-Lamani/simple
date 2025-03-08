arr = [1,2,3,4,5]
n = len(arr) - 1
last_element = arr[n]
for i in range(n , 0 , -1):
    arr[i] = arr[i  - 1]
arr[0] = last_element
print(arr)