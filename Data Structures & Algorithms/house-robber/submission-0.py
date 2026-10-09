class Solution:
    def rob(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        dp = [0] * 2
        dp[0] = nums[0]
        dp[1] = max(nums[0], nums[1])

        for i in range(2, len(nums)):
            temp = dp[1]
            dp[1] = max(temp, nums[i] + dp[0])
            dp[0] = temp
        
        return dp[1]