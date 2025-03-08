def merge_operation_make_palindrome(arr:list) -> int:
    cnt = 0
    n = len(arr)
    if n == 1:
        return 0
    
    i , j = 0 , n -1
    while i  < j:
        if arr[i] == arr[j]:
            i += 1
            j -= 1
            
        elif arr[i] < arr[j]:
            j -= 1
            arr[j] += arr[j +1]
            cnt +=1
        elif arr[i] > arr[j]:
            i += 1
            arr[i] += arr[i -1]
            cnt +=1
    return cnt
        
        
arr = [1, 4, 5, 9, 1]
print(merge_operation_make_palindrome(arr)) 