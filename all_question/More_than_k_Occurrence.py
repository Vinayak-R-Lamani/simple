def countOccurrence(arr:list, k):
    dict ={} 
    n = len(arr)
    count = 0
    for i in arr:
        if i in dict:
            dict[i] += 1
            
        else:
            dict[i] = 1
            
            
    for i , j in dict.items():
        if  j > n //k:
            count += 1
        
    return count

arr =  [1, 4, 7, 7]
k = 2

ans= countOccurrence(arr, k)
print(ans)