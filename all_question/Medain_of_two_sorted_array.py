def median_of_two_sorted_array(a:list , b:list) :
    temp = []
    i ,  j , k = 0 , 0, 0
    n ,m = len(a) , len(b)
    
    while i  < n and j < m:
        if a[i] <= b[j]:
            temp.append(a[i])
            i += 1
        else:
            temp.append(b[j])
            j += 1
            
    while i < n:
        temp.append(a[i])
        i += 1
        
    while j < m:
        temp.append(b[j])
        j += 1
        
    if len(temp) % 2 == 1:
        return temp[len(temp)// 2]
    else:
        return (temp[len(temp) // 2] + temp[(len(temp) // 2) - 1])/2
    
a = [-5, 3, 6, 12, 15]
b= [-12, -10, -6, -3, 4, 10]

# a = [2, 3, 5, 8]
# b = [10, 12, 14, 16, 18, 20]

# a = []
# b = [2, 4, 5, 6]
        
print(median_of_two_sorted_array(a , b))
        
            