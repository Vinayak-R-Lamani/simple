def move(arr:list):
    left , right  = 0 , len(arr) - 1
    
    while left < right:
        
        while left < right and arr[left] <  0:
            left += 1
            
        while right >left and arr[right] > 0:
            right -= 1
            
        if right > left:
            arr[left] , arr[right] = arr[right] , arr[left]
            left += 1
            right -= 1
    return arr

if __name__ == "__main__":
    arr = [-12, 11, -13, -5, 6, -7, 5, -3, -6]
    ans = move(arr)

    for num in ans:
        print(num, end=" ")
    print()