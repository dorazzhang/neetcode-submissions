class Solution:

    # input: 2d array of points, integer k
    # output: 2d array of closest points

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        # want k closest points
        # we can keep a max heap of size k
        # whenever theres a new point that is less than our max, we pop our max out and append the new point so we're always keeping the k smallest points so far
        # helps operations become nlogk + klogk

        heap = []
        for point in points:
            distance = (point[0]**2) + (point[1]**2)

            if len(heap) >= k:
                if distance < -heap[0][0]:
                    heapq.heappop(heap)
                    heapq.heappush(heap, (-distance, point))
                else:
                    continue
            else:
                heapq.heappush(heap, (-distance, point))
        
        return [point for distance, point in heap]
        


        