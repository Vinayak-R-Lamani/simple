def reverse_array(arr:list):
    i  = 0 
    j = len(arr) - 1
    while i<j:
        arr[i] , arr[j] = arr[j] , arr[i]
        i += 1
        j -= 1
    return arr
if __name__ == "__main__":
    arr = [1,2,3,4,5] 
    print(reverse_array(arr))