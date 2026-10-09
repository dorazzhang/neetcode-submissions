class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        # backtracking, go down every possible path depth first search and backtrack when you see that it doesn't work

        ROWS, COLS = len(board), len(board[0])
        path = set()
        # formula for these is to always create a nested dfs in the method
        # base case is what youre searching for
        def dfs(r, c, i):
            if i == len(word):
                return True

            if min(r, c) < 0 or r >= ROWS or c >= COLS or (r,c) in path or word[i] != board[r][c]:
                return False
            
            path.add((r, c))

            res = (dfs(r + 1, c, i+1) or dfs(r - 1, c, i+1) or dfs(r, c+1, i+1) or dfs(r, c-1, i+1))
            path.remove((r, c))
            return res
        
        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False
         
        