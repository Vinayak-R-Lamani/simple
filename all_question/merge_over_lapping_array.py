# arr =  [[1, 3], [2, 4], [6, 8], [9, 10]]
arr = [[6,8],[1,9],[2,4],[4,7]]
arr.sort()
i = 1
n = len(arr)
while i < n:
    prev = arr[i - 1][1]
    cur  = arr[i ] [ 0]
    if prev >= cur:
        arr[i - 1][1]= max(arr[i][1],arr[i-1][1])
        arr.pop(i)
        n = len(arr)
    else:
        i += 1
        
print(arr)