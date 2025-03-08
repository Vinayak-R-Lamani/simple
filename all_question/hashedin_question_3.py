def get_lowest_rank(arr:list):
    ans = 0
    min_ele = float('inf')
    for i in arr:
        if i < min_ele :
            ans += 1
            min_ele = i
    return ans -1

arr =  [4,3,2,1]
ans = get_lowest_rank(arr)
print(ans)