class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #min heap, keep the top k elements
        self.stream = []
        self.k = k
        for num in nums:
            if len(self.stream) < self.k:
                heapq.heappush(self.stream, num)
            else:
                if num > self.stream[0]:
                    heapq.heappop(self.stream)
                    heapq.heappush(self.stream, num)
                
    def add(self, val: int) -> int:
        if len(self.stream) < self.k:
            heapq.heappush(self.stream, val)
        elif val > self.stream[0]:
            heapq.heappop(self.stream)
            heapq.heappush(self.stream, val)
        
        return self.stream[0]
        
