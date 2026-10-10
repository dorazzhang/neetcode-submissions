class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        
        # add numbers to a heap if max capacity k
        # kth largest is the smallest element out of the k largest
        # if any number is greater than smallest element
        # pop out smallest and add number

        
        heap = []

        for num in nums:
            if len(heap) < k:
                heapq.heappush(heap, num)
            else:
                if num > heap[0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, num)
        
        return heap[0]