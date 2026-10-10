class Solution:
    def jump(self, nums: List[int]) -> int:
        # max length of a jump towards the right form i
        # return minimum number of jumps to reach last position

        # [2, 4, 1, 1, 1, 1]

        # dp[i] = minimum jump to reach pos i [0, 1, 1, 2, 2, 2]

        # O(n^2) time O(n) space solution

        
        # greedy solution

        # store the current range we can reach with x jumps
        # base case, 0 jumps = range 0 to 0
        # while we havent reached the end of array
        # for every elem in array
        # we update farthest index reachable with another jump


        # l = 0
        # r = 0
        # res = 0

        # while r < len(nums) - 1:
        #     farthest = 0
        #     for i in range(l, r + 1):
        #         farthest = max(farthest, i + nums[i])
        #     l = r + 1
        #     r = farthest
        #     res += 1
        
        # return res

        dp = [float("inf")] * len(nums)

        dp[0] = 0

        for i in range(len(nums)):
            for jump in range(1, nums[i] + 1):
                if (i + jump) < len(nums):
                    dp[i + jump] = min(dp[i + jump], dp[i] + 1)
        
        return dp[-1]




            

