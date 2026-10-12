class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        # '1': land
        # '0': water
        # '1's surrounded by '0's is an island

        #intuition: bfs

        # iterate through every cell
        # ignore 0's (water), when we hit an unvisited 1 (land)
        # we run bfs on this island and mark everything as seen (where boundaries are 0s)
        # each time we run bfs, we increment island count by 1

        # every time we visit a 1, we can modify the cell in place to be a 0


        def bfs(r, c, grid):

            q = deque()
            q.append((r, c))
            grid[r][c] = '0'

            while q:
                r, c = q.popleft()
                
                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    if r + dr < 0 or r + dr >= len(grid) or c + dc < 0 or c + dc >= len(grid[0]) or grid[r + dr][c + dc] == '0':
                        continue
                    q.append((r + dr, c + dc))
                    grid[r + dr][c + dc] = '0'
            return 1
        
        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == '1':
                    res += bfs(r, c, grid)

        return res
