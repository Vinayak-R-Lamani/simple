def min_ele(arr:list):
    min_ele =  float('inf')
    for ele in arr:
        if ele < min_ele:
            min_ele = ele
    return min_ele


arr = [3,4,2,5,1,-1,-100000]
print(min_ele(arr)) # -100000
