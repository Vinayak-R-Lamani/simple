class Solution:
    def search(self , nums:list , target:int) -> int:
        start , end = 0  , len(nums) - 1
        ans = -1
        while start <= end:
            mid = (start + end) // 2
            if nums[mid] == target:
                ans =  mid
            if nums[start] <= nums[mid]:
                if nums[start] <= target <= nums[mid]:
                    end = mid - 1
                else:
                    start = mid + 1
            else:
                if nums[mid] <= target <= nums[end]:
                    start = mid + 1
                else:
                    end = mid - 1
                    
        return ans  + 1    
    
if __name__ == "__main__":
    nums = [4,5,6,7,8,0,1,2]
    target = 0
    ans = Solution().search(nums,target)
    print(ans)
    