import heapq
# arr = [1,2,3,5]
# arr.insert(0,6)
# arr.pop(0)

# print(arr)

nums = [3,2,3,1,2,4,5,5,6]
k = 4
# heap = []
# for i in nums:
#     if len(heap) == 0:
#         heap.append(i)
#     else:
#         inserted = 0
#         for j in range(len(heap)):
#             if i < heap[j]:
#                 heap.insert(j,i) 
#                 inserted = 1
#                 break
#         if inserted == 0:
#             heap.append(i)
#     if  len(heap ) > k:
#         heap.pop(0)
        
# print(heap[0])

# heap = []
# for i in nums:
#     heapq.heappush(heap,-i)
#     print(heap)
#     if len(heap) > k:
#         heapq.heappop(heap)
#         print(heap)
# print(-heap[0])

 # max_water = 0
        # l , r = 0 , len(height) - 1
        # while l < r:
        #     w = r - l
        #     h = min(height[r] , height[l])
        #     area = w * h
        #     max_water = max(max_water , area)
        #     if height[l] < height[r]:
        #         l +=1
        #     else:
        #         r -= 1

        # return max_water

        # max_water = 0
        # l , r = 0 , len(height) - 1
        # while l < r:
        #     w = r - l
        #     h = min( height[ l] , height[r])
        #     area = h * w
        #     max_water = max(max_water , area)
        #     if height[l] < height[r]:
        #         l += 1
        #     else:
        #         r -= 1
        # return max_water 
        # max_water = 0
        # l , r = 0 , len(arr) - 1
        # while l < r:
        #     w = r - l
        #     h = min(arr[l] , arr[r])
        #     area = w * h
        #     max_water = max(max_water , area)
        #     if arr[l ] < arr[r]:
        #         l += 1
        #     else :
        #         r -= 1
        # return max_water 
        
        
# n = 10
# print((str(n) * 10) [:10])
# temp = [1]

# print( ord('B'.lower())- ord('a') )

# if not temp:
#         print(True)
# else:
#        print(False) 

# dict = { 'temp' : [1,2,3,4] , 
#         'camp' : [2,3],
#         'samp' : [3]
#         }

# print(dict['temp'])
# dict['temp'].append(5)
# print(dict['temp'])

# ans = [sorted(dict)]
# print(ans)