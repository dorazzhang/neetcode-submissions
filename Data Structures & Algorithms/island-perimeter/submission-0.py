class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        # m * n grid where 1 = land and 0 = water

        # connected horizontally/vertically
        # exactly one island
        # boundaries are outside of grid
        
        # we want to find an edge of the island and count the sides of the island
        # a side is a cell of land that touches water

        # find first land occurance and run dfs on it

        # split up cases for not being able to advance & counting a perimeter
        # when we go in a direction out of bounds or water 
            # 1. increment perimeter count, 2. not go that way
        # when we go in a direction to a visited piece of land already
            # do not go that way, dont increment perimeter count
        

        ROWS = len(grid)
        COLS = len(grid[0])

        visited_land = set()
        perimeter = 0

        def dfs(r, c):
            nonlocal perimeter
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or grid[new_r][new_c] == 0:
                    # defines a perimeter of land
                    perimeter += 1
                else:
                    if (new_r, new_c) not in visited_land:
                        visited_land.add((new_r, new_c))
                        dfs(new_r, new_c)
                    
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 1:
                    visited_land.add((r, c))
                    dfs(r, c)
                    return perimeter
        
        return perimeter