class Solution:
    def rob(self, nums: List[int]) -> int:
        # same as robber 1 but append nums[0] to the end.
        # keep track of if nums[0] was used?
        
        def helper(nums):
            if len(nums) == 1:
                return nums[0]
            dp = [nums[0], max(nums[0],nums[1])]
            for i in range(2, len(nums)):
                temp = dp[1]
                dp[1] = max(temp, dp[0] + nums[i])
                dp[0] = temp
            return dp[1]
        if len(nums) == 1:
            return nums[0]
        return max(helper(nums[1:]), helper(nums[:len(nums) - 1]))