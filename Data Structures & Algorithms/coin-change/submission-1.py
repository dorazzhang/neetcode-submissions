class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        # dp[0] = 0, takes 0 coins to sum to 1
        # dp[1] = 1

        # dp[2] = 1 + dp[1]

        dp = [float("inf")] * (amount + 1)
        dp[0] = 0

        for a in range(1, amount + 1):
            for c in coins:
                if a - c >= 0:
                    dp[a] = min(dp[a], 1 + dp[a - c])
        return dp[amount] if dp[amount] != float("inf") else -1

