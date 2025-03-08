def maximum_product_subarray(arr:list) -> int :
    ans = 0
    n = len(arr)
    left = [1] * n
    right = [1] *n
    
    left[0] = arr[0]
    right[n - 1] = arr[ n- 1]
    for i in range(1 ,n):
        left[i] =  left[i - 1] * arr[i]
        
    for i in range(n - 2 , -1, -1):
        right[i] = right[ i + 1] * arr[i]
        
    for i in range(n):
        ans = max(ans , left[i] , right[i])
        
    return ans

nums = [-2,0,-1]
ans = maximum_product_subarray(nums)
print(ans)