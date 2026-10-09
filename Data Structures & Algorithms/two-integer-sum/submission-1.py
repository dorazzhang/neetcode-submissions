class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        s = {}

        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in s:
                return [s[diff], i]
            else:
                s[nums[i]] = i
        return None
            
