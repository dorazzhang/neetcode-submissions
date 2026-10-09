class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # ones = 0
        # curr = 0
        # for i in range(len(nums)):
        #     while i < len(nums) and nums[i] == 1:
        #         curr += 1
        #         i += 1
        #     ones = max(ones, curr)
        #     curr = 0
        # return ones

        left = 0
        ones = 0
        for r in range(len(nums)):
            if nums[r] == 0:
                ones = max(ones, r - left)
                left = r + 1
        
        ones = max(ones, len(nums) - left)
        return ones
            
            
        