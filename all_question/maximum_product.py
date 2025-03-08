def Brute_maxProductSubArray(nums):
    result = float('-inf')
    for i in range(len(nums)-1):
        for j in range(i + 1 , len(nums)):
            prod = 1
            for k in range(i , j +1):
                prod *= nums[k]
            result = max(result , prod)
            
    print(result)
    
def Batter_maxProductSubArray(nums: list):
    result = nums[0]
    for i in range(len(nums) - 1):
        p = nums[i]
        for j in range(i+1 , len(nums)):
            result = max(result , p)
            p *= nums[j]
        result = max(result , p)
    print(result)        
    
def optimal_maxProductSubArray(nums: list):
    n = len(nums)
    pre , suff =1,1
    ans = float('-inf')
    for i in range(n):
        if pre == 0:
            pre = 1
        if suff == 0:
            suff = 1
        pre *= nums[i]
        suff *= nums[n-i-1]
        ans = max(ans,max(pre, suff))
    print(ans)
        

if __name__ == "__main__":
    arr = [1,-2,-2,0,-4,-5]
    optimal_maxProductSubArray(arr)