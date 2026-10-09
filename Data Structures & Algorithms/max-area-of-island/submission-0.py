class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        # visit every cell, maintain visited set
        # if cell is 1, start dfs and count # of connecting cells
        # store max count seen so far

        visited = set()
        res = 0
        directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
        ROWS, COLS = len(grid), len(grid[0])

        def dfs(r, c):
            if (r < 0 or c < 0 or r >= ROWS or
                c >= COLS or grid[r][c] == 0 or (r, c) in visited
            ):
                return 0

            visited.add((r, c))
            count = 1
            for dr, dc in directions:
                count += dfs(r + dr, c + dc)
            return count

        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    continue
                else:
                    count = dfs(r, c)
                    res = max(res, count)
        return res
        