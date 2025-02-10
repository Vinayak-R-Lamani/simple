def remove_duplicates_sort_arr(arr:list):
    n = len(arr)
    j = 0
    for i in range(1, n ):
       if arr[i] != arr[j]:
              j += 1
              arr[j] = arr[i]
            
    print(arr)
    
if __name__ == "__main__":
    arr =[1,1,2,2,2,3,3]    
    remove_duplicates_sort_arr(arr)
    