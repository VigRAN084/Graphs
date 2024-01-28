import heapq

arr = [5, 4, 3, 2, 1]
arr = [-x for x in arr]

# Converts list to minheap
heapq.heapify(arr)
print(arr)
heapq.heappop(arr)

    