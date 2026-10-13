class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # grid where 0 (water) or 1 (land)
        #island - group of land connected
        # outside of grid is out of bounds
        # area = number of cells in island (# of 1s)
        # return max area
        # if no islands return 0
        # only getting ones and zeros
        # ints
        # m * n

        # track which cells/islands you've already visited
        # maintain a global maximum
        # use dfs/bfs to traverse when you encounter an island

        # iterate through all cells in grid
        # when encounter a 1, run bfs (returns count)
            # inside bfs, we are changing encountered 1 -> 0
        # return max from bfs's that we've ran

        max_area = 0

        ROWS = len(grid) # 4
        COLS = len(grid[0]) # 5

        # traverses an island and returns its area
        def dfs(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS or grid[r][c] == 0:
                return 0
            else:
                grid[r][c] = 0
                return 1 + dfs(r + 1, c) + dfs(r - 1, c) + dfs(r, c + 1) + dfs(r, c - 1)

        for r in range(ROWS): # nested for loop, O(n * m)
            for c in range(COLS):
                if grid[r][c] == 1: # encountered island
                    max_area = max(max_area, dfs(r, c)) # 6
        
        return max_area