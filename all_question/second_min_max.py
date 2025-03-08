def second_smallest_element(arr:list):
    smallest,second_smallest_ele = float('inf'),float('inf')
    for ele in arr:
        if ele < smallest:
            second_smallest_ele = smallest
            smallest = ele
        elif ele < second_smallest_ele and ele != smallest:
            second_smallest_ele = ele
            
    return second_smallest_ele

def second_largest_element(arr: list):
    largest , second_largest_ele = float('-inf') ,float('-inf')
    for ele in arr:
        if ele  > largest:
            second_largest_ele = largest
            largest = ele
        elif ele > second_largest_ele and ele != largest:
            second_largest_ele = ele
            
    return  second_largest_ele   



arr = [3,4,2,5,1,-1,-100000]
print(second_largest_element(arr))
            