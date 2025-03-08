import heapq
arr = [7, 10, 4, 3, 20, 15]
k = 3
heap = []
for i in arr:
    heapq.heappush(heap, -i)
    if len(heap) > k:
        heapq.heappop(heap)
        
print(-heap[0])