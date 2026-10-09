class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        diff = dict()
        for i, num in enumerate(nums):
            if num in diff:
                return [diff[num], i]
            diff[target - num] = i
