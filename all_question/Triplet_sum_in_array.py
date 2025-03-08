def Triplet_sum_in_arr(arr:list ,k :int):
    n = len(arr)
    arr.sort()
    i, j ,k = 0 , 0 ,  0
    while i < n and j < n and k < n:
        if i == j or j == k or k == i:
            continue
        
        # if arr[i]