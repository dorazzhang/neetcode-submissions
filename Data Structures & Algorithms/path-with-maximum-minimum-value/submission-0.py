class Solution:
    def maximumMinimumPath(self, grid: List[List[int]]) -> int:
        
        # dijkstras but storing the minimum score in path so far, wanting the maximum way to get to each node

        # usually: heap stores sum of weights -> minimum weight
        # heap pops out min -> heap pops out max

        # start at (0,0)
        maxHeap = [(-grid[0][0],0,0)] # store negatives for max isntead of min     
        visited = {}

        while maxHeap:
            score1, r1, c1 = heapq.heappop(maxHeap)
            score1 *= -1

            visited[(r1, c1)] = score1
            
            directions = [(1,0), (-1,0), (0,1), (0,-1)]

            for dr, dc in directions:
                if r1 + dr < 0 or r1 + dr >= len(grid) or c1 + dc < 0 or c1 + dc >= len(grid[0]) or (r1 + dr, c1 + dc) in visited:
                    continue
                score2 = min(score1, grid[r1 + dr][c1 + dc])
                heapq.heappush(maxHeap, (-score2, r1 + dr, c1 + dc))
        
        return visited[(len(grid) - 1, len(grid[0]) - 1)]
                