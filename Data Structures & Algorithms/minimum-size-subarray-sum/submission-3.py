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
        curr_sum = 0

        for r in range(len(nums)):
            curr_sum += nums[r]
            while curr_sum >= target:
                res = min(res, r - l + 1)
                curr_sum -= nums[l]
                l += 1
                if l > r:
                    break

        return 0 if res == float('inf') else res
            