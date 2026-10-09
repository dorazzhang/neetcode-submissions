class Solution:
    def climbStairs(self, n: int) -> int:
        # at each step, you either move one or two steps

        # top down
        # cache = [-1] * n
        # def dfs(i, cache):
        #     if i > n:
        #         return 0
        #     if i == n:
        #         return 1
        #     if cache[i] != -1:
        #         return cache[i]
        #     cache[i] = dfs(i + 1, cache) + dfs(i + 2, cache)
        #     return cache[i]
        
        # return dfs(0, cache)

        # bottom up

        if n <= 2:
            return n
        dp = [0] * 2
        dp[0], dp[1] = 1, 2

        for i in range(2, n):
            temp = dp[1]
            dp[1] = dp[0] + temp
            dp[0] = temp
        return dp[1]

        