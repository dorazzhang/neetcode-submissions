class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        # 0: empty
        # 1: fresh
        # 2: rotten

        # every minute, adjacent fresh to rotten fruit become rotten
        # min number of minutes until there are zero fresh fruits

        # simultaneous bfs where you store number of levels traversed

        ROWS = len(grid)
        COLS = len(grid[0])

        queue = deque()
        visited = set()
        count_fresh = 0
        count_rotten = 0

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                    visited.add((r, c))
                    count_rotten += 1
                if grid[r][c] == 1:
                    count_fresh += 1
        
        if count_fresh == 0:
            return 0
        
        minutes = 0
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and (new_r, new_c) not in visited and grid[new_r][new_c] != 0:
                        queue.append((new_r, new_c))
                        visited.add((new_r, new_c))
                
            minutes += 1
        
        if (count_fresh + count_rotten) > len(visited):
            return -1
        
        return minutes - 1


        