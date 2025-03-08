def Rotate_array_k(arr:list , k:int,direction:str):
    n = len(arr)
    k %= n
    arr.reverse()
    if direction == "right":
        arr[:k] = reversed(arr[:k])
        arr[k:] = reversed(arr[k:])
    else:
        arr[n-k:] = reversed(arr[n-k:])
        arr[:n-k] = reversed(arr[:n-k])
    print(arr)
    
    
def reverse(arr,start, end):
    while start < end:
        arr[start] , arr[end] = arr[end] , arr[start]
        start += 1
        end -= 1
        
def rotate_array_in_place(arr:list, k:int , direction = 'right'):
    n = len(arr)
    k %= n
    
    if direction == 'right':
        reverse(arr, 0 , n -1)
        reverse(arr, 0, k-1)
        reverse(arr, k , n -1)
    else:
        reverse(arr,0,k -1)
        reverse(arr,k ,n -1)
        reverse(arr, 0 , n -1)
        
    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    k = 3
    rotate_array_in_place(arr, k , "left")
    print(arr)