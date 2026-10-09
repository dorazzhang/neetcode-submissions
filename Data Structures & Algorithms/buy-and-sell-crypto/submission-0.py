class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        b, s = 0, 1
        ans = 0
        while b < len(prices) - 1 and s < len(prices):
            profit = prices[s] - prices[b]
            if profit > ans:
                ans = profit
            if prices[b] > prices[s]:
                b = s
                s = b + 1
            else:
                s += 1
        return ans
        