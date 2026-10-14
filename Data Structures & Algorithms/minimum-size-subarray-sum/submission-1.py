class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # positive integers
        # pos target
        # minimal length of subarray whose sum greater than or equal to target
        # order matters
        # not sorted

        # try valid windows where condition is met and store min length
        # then shrink by one
        # if sum too large, shrink
        # if sum too small, extend

        l = 0
        r = 0
        res = float("inf")
        curr_sum = nums[0]

        while r < len(nums) and l < len(nums):
            if curr_sum >= target:
                res = min(res, r - l + 1)
                curr_sum -= nums[l] if l < len(nums) else 0
                l += 1
                if l > r: # this means there was a valid sum of length 1, in which there can't be a better answer
                    break
            else: # sum is less than target
                r += 1
                curr_sum += nums[r] if r < len(nums) else 0
        
        return 0 if res == float("inf") else res