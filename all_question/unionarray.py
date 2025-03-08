def findUnion(a, b):
    a.sort()
    b.sort()
    union = []
    n = len(a)
    m = len(b)
    i , j = 0 , 0
    while i < n and j < m :
        if a[i] < b[j]:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i +=1
        elif a[i] > b[j]:
            if not union or union[-1] != b[j]:
                union.append(b[j])
            j +=1 
        else:
            if not union or union[-1] != a[i]:
                union.append(a[i])
            i +=1
            j +=1
        
    while i < n:
        if not union or union[-1] != a[i]:
                union.append(a[i])
        i +=1
    
    while j < m:
        if not union or union[-1] != b[j]:
                union.append(b[j])
        j +=1
        
    return union

        
a = [85, 25, 1, 32, 54, 6]
b = [85, 2] 
ans = findUnion(a, b)
print(len(ans))  # Output: [1, 2, 3, 4, 5, 6, 7]
