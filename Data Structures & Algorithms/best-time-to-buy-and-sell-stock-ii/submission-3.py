class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # buy or sell stock
        # can buy then immediately sell
        # allowed to perform any number of transactions
        # can hold at most one share at once
        # return max profit you can achieve

        res = 0

        # base case is dp[0] = 0
        # dp state is basically saying whats the max profit i can make on day i
        # recurring on the profit you can make if you sell on the current day w a previous buy day
        # ans is dp[len(prices) - 1]


        profit = 0

        for i in range(1, len(prices)):
            profit += max(0, (prices[i] - prices[i - 1]))
        
        return profit





