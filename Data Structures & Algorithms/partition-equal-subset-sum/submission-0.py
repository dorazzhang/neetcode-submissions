class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        # array of pos ints
        # true if can partition into two subsets where the sums are equal
        # otherwise false

        # subsets as in order doesn't matter

        # you know sum(subset1) and sum(subset2) has to be total_sum / 2
        # if its not divisible, return false

        total_sum = sum(nums)
        if total_sum % 2 != 0:
            return False

        target = total_sum / 2 # 5

        # if you find one subset that equals target, you know the rest of the values are in the other subset
        # goal is just to find numbers in array adding to target

        def recurse(curr_sum, i): # given current index in array and target, return true if curr_sum + index = target
            nonlocal target
            nonlocal nums
            if i >= len(nums): # once we went through whole array, partition not possible
                return False
            if curr_sum + nums[i] == target: # found partition
                return True
            if curr_sum + nums[i] > target: # can't use nums[i] if over target
                return recurse(curr_sum, i + 1)
            if curr_sum + nums[i] < target: # either use or don't use nums[i]
                return recurse(curr_sum + nums[i], i + 1) or recurse(curr_sum, i + 1)
        
        return recurse(0, 0)

