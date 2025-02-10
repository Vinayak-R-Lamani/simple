from collections import Counter 

arr = [1, 2, 3, 2, 4, 3, 1, 2]
# fre_cnt = Counter(arr)
# sorted_arr = sorted(arr, key = lambda x: (-fre_cnt[x], arr.index(x)))
# print(sorted_arr)
sorted_arr = sorted(arr, key = lambda x:x > 2)
print(sorted_arr)