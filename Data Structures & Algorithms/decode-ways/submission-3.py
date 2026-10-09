class Solution:
    def numDecodings(self, s: str) -> int:

        # # memoization
        # def dfs(i: int, cache) -> int:
        #     if i == len(s):
        #         return 1
        #     if s[i] == "0":
        #         return 0
        #     if cache[i] != -1:
        #         return cache[i]
        #     res = dfs(i + 1, cache)
        #     if i < len(s) - 1:
        #         if s[i] == "1" or s[i] == "2" and s[i+1] <= "6":
        #             res += dfs(i + 2, cache)
        #     cache[i] = res
        #     return res
        # cache = [-1] * len(s)
        # return dfs(0, cache)
        dp = [1] * (len(s) + 1)
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "0":
                dp[i] = 0
            else:
                dp[i] = dp[i + 1]
            if i < len(s) - 1:
                if s[i] == "1" or s[i] == "2" and int(s[i+1]) <= 6:
                    dp[i] += dp[i + 2]
        return dp[0]
