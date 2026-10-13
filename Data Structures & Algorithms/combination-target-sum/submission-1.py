class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        # return list of all unique combinations of nums where numbers sum to target

        # same number can be chosen


        # at every point, check if equals sum
        # if exceeds sum, return (deadend)
        # if less than sum, keep trying more numbers
        # how to handle different orders of the same combination?

        # once we decide not to use a number, we never try to use it again

        nums.sort()
        res = []

        def dfs(i, comb, total): # index, current combination, sum
            if total == target:
                res.append(comb.copy())
                return
            elif i >= len(nums) or total + nums[i] > target:
                return
            else:
                comb.append(nums[i])
                dfs(i, comb, total + nums[i])
                comb.pop()
                dfs(i + 1, comb, total)
        
        dfs(0, [], 0)
        return res

