#First Method
def kLarge(arr,k):
    arr.sort(reverse=True)
    return arr[k-1]

#Second Method
def kLarge(arr,k):
    for i in range(k-1):
        arr.remove(max(arr))
    return max(arr)
  
#Third Method (using Heaps)
import heapq

def kLarge(arr, k):
    arr = [-ele for ele in arr]
    heapq.heapify(arr)
    for i in range(k-1):
        heapq.heappop(arr)
    return -heapq.heappop(arr)
