def check_subset(arr1, arr2):
    # ans = False
    # n = len(arr1)
    # m = len(arr2)
    # arr1.sort()
    # arr2.sort()
    # if n > m:
    #     print(False)
    # else:
    #     i = 0
    #     for j in range(n , m):
    #         if arr1 == arr2[i:j]:
    #             ans = True
    #         else:
    #             i += 1
    #     print(ans)
    ans = 'in'
    for i in arr1:
        if i not in arr2:
            ans = 'not'
            
    print('not')if ans == 'not'else print('in')
        
if __name__ == "__main__":
    arr1 = [12,15,16,13]
    arr2 = [11,12,13,15,16]
    
    check_subset(arr1, arr2)