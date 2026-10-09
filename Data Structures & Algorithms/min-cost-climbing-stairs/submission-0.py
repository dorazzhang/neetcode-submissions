class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        # cost[i] cost of taking step from ith floor
        # either i + 1 or 1 + 2 floor
        # can either start at 0 or 1

        # dp[i] represents minimum cost to reach step i
        # base case dp[0] = 0
        # base case dp[1] = 0

        # recurrence on most recent step
        # dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])

        n = len(cost) + 1
        dp = [float("inf")] * n

        dp[0] = 0
        dp[1] = 0

        for i in range(2, n): # 4
            dp[i] = min(dp[i - 1] + cost[i - 1], dp[i - 2] + cost[i - 2])
        
        return dp[n - 1]