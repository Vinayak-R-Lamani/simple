def kadanes_algo(arr:list):
    max_sum = 0
    curr = 0
    for i in arr:
        curr += i
        max_sum = max(max_sum,curr)
        curr = max(curr , 0)
        
    return max_sum

if __name__ == "__main__":
    nums = [5,4,-1,7,8]
    ans = kadanes_algo(nums)
    print(ans)