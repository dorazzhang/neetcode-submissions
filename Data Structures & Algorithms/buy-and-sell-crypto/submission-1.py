class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # b, s = 0, 1
        # ans = 0
        # while b < len(prices) - 1 and s < len(prices):
        #     profit = prices[s] - prices[b]
        #     if profit > ans:
        #         ans = profit
        #     if prices[b] > prices[s]:
        #         b = s
        #         s = b + 1
        #     else:
        #         s += 1
        # return ans

        # dp version

        min_so_far = prices[0]
        ans = 0
        for sell in prices:
            ans = max(ans, sell - min_so_far)
            min_so_far = min(min_so_far, sell)
        return ans
        