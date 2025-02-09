def max_ele(arr:list):
    max_ele = float('-inf')
    for ele in arr:
        if ele > max_ele:
            max_ele = ele
    return max_ele

arr = [1, 2, 3, 4, 5]
print(max_ele(arr))