# arr = [4,5,3,7,2,11]
arr = [4,6,2,7,19,34]
ans  = [0] * len(arr)

i = 0
j = 1
while j < len(arr):
    if arr[i] < arr[j]:
        ans[i ] = arr[j]
        i += 1
    else:
        while i + 1 <  j:
            ans[i] = ans[i  - 1]
            i += 1
            
    j += 1
    
print(ans)
        

