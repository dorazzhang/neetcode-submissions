class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid: # if grid is empty, no islands
            return 0
        
        # get number of rows and cols in grid
        rows, cols = len(grid), len(grid[0])
        # initialize set to track visited squares
        visit = set()

        # keep track of islands counted so far
        islands = 0

        def bfs(r, c):
            # intialize queue for bfs
            q = collections.deque()
            # add starting point to visit
            visit.add((r, c))
            # add starting point to queue
            q.append((r, c))

            # while queue not empty
            while q:
                # pop value from queue
                row, col = q.popleft()
                
                # possible ways to travel through grid
                directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                # for all 4 ways to go in
                for dr, dc in directions:
                    # new square after going up, down, left, or right
                    r, c = row + dr, col + dc
                    # if the square is in bounds and value is 1 and not visited before, append to queue and mark as visited
                    if (r in range(rows) and c in range(cols) and grid[r][c] == "1" and (r, c) not in visit):
                        q.append((r, c))
                        visit.add((r,c))
            # while loop will break once the whole island was visited

        # for every square in grid,
        for r in range(rows):
            for c in range(cols):
                # if the square is water, it will just keep looping through. only calls bfs to go through the land squares
                # if we see a 1 that hasn't been visited yet
                if grid[r][c] == "1" and (r, c) not in visit:
                    # run bfs to cover entire island
                    bfs(r, c)
                    # add 1 to island count
                    islands += 1
        return islands

        