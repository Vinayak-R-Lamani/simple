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

heap = []
for i in nums:
    heapq.heappush(heap,-i)
    print(heap)
    if len(heap) > k:
        heapq.heappop(heap)
        print(heap)
print(-heap[0])