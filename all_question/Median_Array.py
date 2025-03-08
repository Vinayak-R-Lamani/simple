def medain_array(arr:list):
    arr.sort()
    n = len(arr)
    
    if (n % 2) == 1:
        return arr[n // 2]
    else:
        return (arr[n // 2] + arr[(n // 2)  - 1]) /2
    
arr = [56, 67, 30, 79]
ans = medain_array(arr)
print(ans)
