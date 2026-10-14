class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        # cell values represent height above sea level
        # top and left are pacific ocean
        # bottom and right are atlantic
        # water can flow updownleftright
        # flow towards equal or lower height and into ocean
        # find all cells where water can flow to both oceans
        # 2d list of all cells in any order

        pacific = set()
        atlantic = set()

        ROWS = len(heights)
        COLS = len(heights[0])

        def dfs(r, c, ocean):
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]

            for dr, dc in directions:
                new_r = r + dr
                new_c = c + dc
                if new_r < 0 or new_r >= ROWS or new_c < 0 or new_c >= COLS or (new_r, new_c) in ocean or heights[new_r][new_c] < heights[r][c]:
                    continue
                else:
                    ocean.add((new_r, new_c))
                    dfs(new_r, new_c, ocean)
        
        for r in range(ROWS):
            pacific.add((r, 0))
            dfs(r, 0, pacific)
        for c in range(COLS):
            pacific.add((0, c))
            dfs(0, c, pacific)

        for r in range(ROWS):
            atlantic.add((r, COLS - 1))
            dfs(r, COLS - 1, atlantic)
        for c in range(COLS):
            atlantic.add((ROWS - 1, c))
            dfs(ROWS - 1, c, atlantic)
        
        res = []
        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in atlantic and (r, c) in pacific:
                    res.append((r, c))
        
        return res
