class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        # for two integers n and k, return all possible combinations of k numbers from range 1,n

        # example, 7, 3

        # 1 2 3 4 5 6 7
        # 1 2 3, 1 3 4, 1 4 5, etc

        # for every number in every pos, we either include or dont include that number

        res = []

        def backtrack(i, comb): # index of curr number we're considering
            if i > n:
                if len(comb) == k:
                    res.append(comb.copy())
                return
            
            comb.append(i) # choice to including it
            backtrack(i + 1, comb)
            comb.pop() # choice not to include it
            backtrack(i + 1, comb)
        
        backtrack(1, [])
        return res