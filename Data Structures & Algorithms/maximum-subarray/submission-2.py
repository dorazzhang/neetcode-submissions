class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #subarray with largest sum and return sum

        # at every position, you either extend your subarray or restart it

        # this is determined by if your subarray is 

        curr_sum = nums[0]
        sum = max(nums)
        for i in range(1, len(nums)):
            curr_sum = max(curr_sum, 0)
            curr_sum += nums[i]
            sum = max(sum, curr_sum)
        return sum