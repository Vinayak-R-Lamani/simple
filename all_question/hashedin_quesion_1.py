# arr = [10,20,30,50,10,70,30]
# k = 0
# max_ans = 0

# for i in range(len(arr) - k - 1):
#     ele = min(arr[i : i + k] )
#     max_ans = max(ele , max_ans)
    
# print(max_ans)

# arr = [10,20,30,50,10,70,30]
arr = [4,5,1,3,2,6,7]
k = 2
max_ans = 0

for i in range(len(arr) -k +1):
    ele = min(arr[i : i + k] )
    print(ele)
    print(arr[i : i + k])
    max_ans = max(ele , max_ans)
    print(max_ans)
print(max_ans)