class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        stones = [-x for x in stones] # O(N) space and time
        heapq.heapify(stones) # (O(N) time)
        # store stones in max heap to access heaviest in logn time

        while len(stones) > 1:
            y = -1 * heapq.heappop(stones) # heaviest stone
            x = -1 * heapq.heappop(stones) # second heaviest
            # if they are equal weight, we dont push either back on
            if x == y:
                continue
            # since x is second heaviest, it gets destroyed, y has new weight y - x
            heapq.heappush(stones, -(y - x))
        return -1 * stones[0] if stones else 0

        