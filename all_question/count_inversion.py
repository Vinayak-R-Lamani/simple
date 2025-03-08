# arr = [2, 4, 1, 3, 5]
# arr = [4,3,2,1]
# # arr.reverse()

# cnt = 0
# for i in range(len(arr) -1):
#     for j in range(len(arr) -1):
#         if arr[i] > arr[j] :
#             cnt += 1

def countAndMerge(arr , l , m , r):
    n1 = m -l + 1
    n2 = r - m
    
    left = arr[l:m + 1]
    right = arr[m + 1 :r + 1]
    
    res = 0 
    i = 0
    j = 0
    k = l
    
    while i < n1 and j < n2:

        # No increment in inversion count
        # if left[] has a smaller or equal element
        if left[i] <= right[j]:
            arr[k] = left[i]
            i += 1
        else:
            arr[k] = right[j]
            j += 1
            res += (n1 - i)
        k += 1

    # Merge remaining elements
    while i < n1:
        arr[k] = left[i]
        i += 1
        k += 1
    while j < n2:
        arr[k] = right[j]
        j += 1
        k += 1

    return res
def countINV(arr , l , r):
    res = 0
    if l < r:
        m = (r + l)//2
        
        res += countINV(arr , l , m)
        res += countINV(arr , m + 1 , r)
        
        res += countAndMerge(arr , l , m , r)
        
    return res
def countInversion(arr):
    return countINV(arr , 0 , len(arr) - 1)
            
# print(cnt)
        