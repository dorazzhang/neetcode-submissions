class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # sum the numbers and return difference

        target_sum = 0
        actual_sum = 0

        for i in range(len(nums)):
            target_sum += (i + 1)
            actual_sum += nums[i]
        
        return target_sum - actual_sum