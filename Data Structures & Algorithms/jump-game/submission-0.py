class Solution:
    def canJump(self, nums: List[int]) -> bool:
        # nums[i] indicates maximum jump

        can_jump = [False] * len(nums)
        [True, True, False, True, True]
        can_jump[len(nums) - 1] = True
        for i in range(len(nums) - 2, -1, -1):
            for j in range(1, nums[i] + 1):
                if can_jump[i + j]:
                    can_jump[i] = True
                    break
        return can_jump[0]