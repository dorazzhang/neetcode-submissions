class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        curr_min = 1
        curr_max = 1
        res = max(nums)
        
        for i in range(len(nums)):
            temp = curr_max * nums[i]
            curr_max = max(curr_min * nums[i], curr_max * nums[i], nums[i])
            curr_min = min(curr_min * nums[i], temp, nums[i])
            res = max(curr_max, res)
        return res
