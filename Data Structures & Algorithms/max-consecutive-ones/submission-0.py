class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        ones = 0
        curr = 0
        for i in range(len(nums)):
            while i < len(nums) and nums[i] == 1:
                curr += 1
                i += 1
            ones = max(ones, curr)
            curr = 0
        return ones
            
            
        