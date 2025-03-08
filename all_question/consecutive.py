arr =  [15, 13, 12, 14, 11, 10, 9]
# arr = [100, 4, 200, 1, 3, 2]

def longestConsecutive(arr):
    arr = sorted(set(arr))
    total_consecutive = 1
    consecutive= 1
    
    i = 1
    while i < len(arr) :
        if arr[i]  == arr[i -1] + 1:
            consecutive += 1
            
        else:
            total_consecutive = max(total_consecutive , consecutive)
            consecutive = 1
        i += 1
            
    return max(consecutive, total_consecutive) 

def longestConsecutive_2(arr:list):
    arr.sort()
    ans = []
    total_len= 0
    for i in range(len(arr)): 
        if not ans or ans[-1] == arr[i] - 1:
            ans.append(arr[i])
            total_len = max ( total_len , len(ans))
            
        else:
            ans.clear
            
    return total_len
            
            
    

ans = longestConsecutive_2(arr)
print(ans)