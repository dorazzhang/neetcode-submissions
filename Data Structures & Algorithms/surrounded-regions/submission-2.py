class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # X
        # O

        # iterate through every element in the grid
        # if x, mark as visited and do nothing
        # if o, start dfs
        # if any o's are edges, dont do anything except mark visited
        # if dfs is done from just reaching x's, backtrack to start and change every o to x along the way

        queue = deque()
        ROWS = len(board)
        COLS = len(board[0])

        uncaptured = set()

        for c in range(COLS):
            if board[0][c] == 'O':
                uncaptured.add((0, c))
                queue.append((0, c))
            if board[ROWS - 1][c] == 'O':
                uncaptured.add((ROWS - 1, c))
                queue.append((ROWS - 1, c))
        
        for r in range(1, ROWS - 1):
            if board[r][0] == 'O':
                uncaptured.add((r, 0))
                queue.append((r, 0))
            if board[r][COLS - 1] == 'O':
                uncaptured.add((r, COLS - 1))
                queue.append((r, COLS - 1))
        
        while queue:
            for i in range(len(queue)):
                
                r, c = queue.popleft()

                directions = [(1,0), (-1,0), (0, 1), (0, -1)]

                for dr, dc in directions:
                    new_r = r + dr
                    new_c = c + dc

                    if new_r > 0 and new_r < ROWS and new_c > 0 and new_c < COLS and (new_r, new_c) not in uncaptured and board[new_r][new_c] != 'X':
                        uncaptured.add((new_r, new_c))
                        queue.append((new_r, new_c))
        
        for r in range(1, ROWS - 1):
            for c in range(1, COLS - 1):
                if board[r][c] == 'O' and (r, c) not in uncaptured:
                    board[r][c] = 'X'
        