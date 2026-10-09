class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones]
        heapq.heapify(stones)

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones) # heaviest stone
            x = -1 * heapq.heappop(stones) # second heaviest
            if x == y:
                continue
            if x < y:
                heapq.heappush(stones, -(y - x))
        return -1 * stones[0] if stones else 0

        