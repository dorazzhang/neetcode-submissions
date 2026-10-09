class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        # store two sets
        # check off the overlap

        # starting from every ocean cell

        ROWS, COLS = len(heights), len(heights[0])

        pac, atl = set(), set()

        def dfs(r, c, visited, prev_r, prev_c):
            if (r, c) in visited or r < 0 or c < 0 or r >= ROWS or c >= COLS or heights[prev_r][prev_c] > heights[r][c]:
                return
            directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
            visited.add((r, c))
            for direction in directions:
                dfs(r + direction[0], c + direction[1], visited, r, c)
        
        res = []
        for c in range(COLS):
            dfs(0, c, pac, 0, c)
            dfs(ROWS - 1, c, atl, ROWS - 1, c)
        
        for r in range(ROWS):
            dfs(r, 0, pac, r, 0)
            dfs(r, COLS - 1, atl, r,COLS - 1)
        
        res = []

        for r in range(ROWS):
            for c in range(COLS):
                if (r, c) in pac and (r, c) in atl:
                    res.append([r, c])
        return res
