def Minimum_jumps(arr:list):
    cnt = 0
    for i in range(len(arr)):
        if i > cnt:return False
        cnt = max(cnt , i + arr[i])
        print(cnt)
        
    return cnt
        
arr = [1, 3, 5, 8, 9, 2, 6, 7, 6, 8, 9]
ans = Minimum_jumps(arr)
print(ans)