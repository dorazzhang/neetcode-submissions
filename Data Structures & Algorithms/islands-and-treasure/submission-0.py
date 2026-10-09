class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        
        # -1: water cell
        # 0: treasure
        # INF - land

        # fill each land cell w distance to nearest treasure else INF
        # up, down, left, right
        # in place

        # for every land cell, explore every possible path using bfs and return distance immediately when treasure is found

        # O((m * n)^ 2)

        # better idea, bfs from every single treasure simultaneously (kind of like they're a non zero level in a regular bfs algorithm)

        # mark land as visited as soon as they are seen by any treasure and this is automatically the shortest distance

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()

        queue = deque()

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 0:
                    visited.add((r, c))
                    queue.append((r, c))
        
        distance = 0
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while queue:
            for i in range(len(queue)):
                r, c = queue.popleft()

                grid[r][c] = distance

                for x, y in directions:
                    new_r = r + x
                    new_c = c + y
                    if new_r >= 0 and new_r < ROWS and new_c >= 0 and new_c < COLS and (new_r, new_c) not in visited and grid[new_r][new_c] != -1:
                        visited.add((new_r, new_c))
                        queue.append((new_r, new_c))
            
            distance += 1






