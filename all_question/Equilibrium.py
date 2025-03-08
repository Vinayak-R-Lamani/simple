def find_equilibrium_index(arr: list):
    # total_sum = sum(arr)
    # left_sum = 0
    # ans = 0
    # for i , num in enumerate(arr):
    #     total_sum -= num
    #     if left_sum == total_sum:
    #         ans = i
    #     left_sum += num
        
    # print(-1) if ans == 0 else print(ans)
    total_sum = sum(arr)
    left_sum = 0
    ans = 0
    for i , num in enumerate(arr):
        total_sum -= num
        if left_sum == total_sum:
            ans = i
        left_sum += num
    print(-1) if ans == 0 else print(ans)
    
if __name__ == "__main__":
    nums = [2,3,-1,8,4]
    # nums = [1,-1,4]
    find_equilibrium_index(nums)
    