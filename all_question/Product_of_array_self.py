nums = [1,2,3,4]
ans = [1] * len(nums)
prefix = 1
suffix = 1
# for i in range(len(nums)):
#     product = 1
#     for j in range(len(nums)):
#         if i == j:
#             continue
#         product *= nums[j]
        
#     ans[i] = product
j = 0
for i in nums:
    ans[j] = prefix
    prefix *= i
    j += 1
print(ans)

for i in range(len(nums) -1  , -1 , -1):
    ans[i] *= suffix
    suffix *= nums[i]

print(ans)