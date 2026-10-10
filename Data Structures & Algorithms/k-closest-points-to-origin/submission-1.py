class Solution:

    # input: 2d array of points, integer k
    # output: 2d array of closest points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        for point in points:
            distance = (point[0]**2) + (point[1]**2)

            heapq.heappush(heap, (distance, point))
        
        res = []

        for _ in range(k):
            res.append(heapq.heappop(heap)[1])
        
        return res
        


        