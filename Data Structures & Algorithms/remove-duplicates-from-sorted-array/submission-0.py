class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # can have two pointers
        # left pointer stays at the second reoccurence
        # right pointer moves to the next unique char
        # perform swap
        # then increment left pointer and continue

        left = 0
        right = 0

        for right in range(1, len(nums)):
            if nums[left] != nums[right]:
                left += 1
                nums[left] = nums[right]
        
        return left + 1