def rotate_element(arr:list,k:int):
    n = len(arr)
    k = k % n
    
    arr.reverse()
    arr[:k] = reversed(arr[:k])
    arr[k:] = reversed(arr[k:])
    
    print(arr)
    
if __name__ == "__main__":
    arr = [1,2,3,4,5,6]
    k = 3
    rotate_element(arr, k)
    