def sort012(arr):
        # code here
        count_1 , count_0 , count_2 = 0 ,0, 0
        for i in arr:
            if i == 0:
                count_0 +=1
            elif i == 1:
                count_1 +=1
            else:
                count_2 +=1
                
        for i in range(0 , count_0):
            arr[i] = 0
        for i in range(count_0 , count_1  + count_0):
            arr[i] = 1
        for i in range(count_1 + count_0,count_1 + count_0 + count_2):
            arr[i] = 2
        return arr
    
def sort_0_1_2(arr:list):
    low , mid , height = 0 ,0, len(arr) - 1
    
    while mid  <= height:
        if arr[mid] == 0:
            arr[low] , arr[mid] = arr[mid] , arr[low]
            low +=1
            mid +=1
            
        elif arr[mid] == 1:
            mid +=1 
        else:
            arr[height] , arr[mid] = arr[mid] ,arr[height]
            height -= 1
    return arr
    
        
        
            
            
arr = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]
arr =sort_0_1_2(arr)
print(arr)