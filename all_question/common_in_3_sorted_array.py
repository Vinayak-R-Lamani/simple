def commonElement(arr1, arr2, arr3):
    i , j , k = 0, 0 ,0
    n1, n2, n3 = len(arr1) , len(arr2) , len(arr3)
    
    result = []
    
    while i < n1  and j < n2  and k < n3:
        if arr1[i] == arr2[j] == arr3[k]:
            if not result or result[-1] != arr1[i]:
                result.append(arr1[i])
            i +=1
            j +=1
            k +=1
            
        elif arr1[i] < arr2[j]:
            i += 1
        elif arr2[j] < arr3[k]:
            j += 1
        else:
            k += 1
    
    return result if result else [-1]

# arr1 = [1, 5, 10, 20, 40, 80] 
# arr2 = [6, 7, 20, 80, 100]
# arr3 = [3, 4, 15, 20, 30, 70, 80, 120]
arr1 = [1, 1, 1, 2, 2, 2]
arr2 = [1, 1, 2, 2, 2]
arr3 = [1, 1, 1, 1, 2, 2, 2, 2]

ans = commonElement(arr1 , arr2 , arr3)

print(ans)

# dict = {}
# ans = []

# for i in arr1:
#     dict[i]= 1
    
# for i in arr2:
#     if i in dict and dict[i] == 1:
#         dict[i] = 2
    
# for i in arr3:
#     if i in dict and dict[i] == 2:
#         dict[i] == 3
#         # ans.append(i)
        
# for i ,j in dict.items():
#     if j == 3:
#         ans.append(i)
    
    

# print(ans)


