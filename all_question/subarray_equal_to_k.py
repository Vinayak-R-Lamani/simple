arr = [1,2,3]
# prefix_map ={0:1}
# prefix_sum = 0
k = 3

# cnt = 0

# for i in arr:
#     prefix_sum += i
#     if prefix_sum - k  in prefix_map:
#         cnt += prefix_map[prefix_sum - k]
        
#     prefix_map[prefix_sum] = prefix_map.get(prefix_sum , 0) + 1
    
# print(cnt)
cnt = 0
for i in range(len(arr)):
    sum_ =0
    for j in range(i ,len(arr)):
        sum_ += arr[j]
        if sum_ == k:
            cnt += 1
            
print(cnt)

