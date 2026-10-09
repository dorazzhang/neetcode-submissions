class Solution:
    def numSquares(self, n: int) -> int:

        # dynamic programming
        # worst case is all 1's, initialize a dp array of n
        # dp[n] = least amount of perfect squares to sum up to n
        # base case = dp[0] is 0, dp[1] is 1
        # try all possible perfect squares less than target and take the minimum

        dp = [n] * (n + 1)
        dp[0] = 0
        dp[1] = 1

        for i in range(2, n + 1):
            s = 1
            while s*s <= i:
                dp[i] = min(dp[i], 1 + dp[i - (s * s)])
                s += 1
        return dp[n]
        
        # 0 1 2 3 1 
        