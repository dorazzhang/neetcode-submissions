class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:
        nums.sort()
        res = 0
        for i in range(len(nums) - 2):
            new_target = target - nums[i]
            res += self.twoSumSmaller(nums, i + 1, new_target)
        return res


    def twoSumSmaller(self, nums: List[int], start: int, target: int) -> int:
        
        res = 0
        left = start
        right = len(nums) - 1
        while left < right:
            if nums[left] + nums[right] < target:
                # if smallest + biggest is less than target,
                # all the other combinations using smallest and values betwene smallest to biggest will also be less than target
                res += right - left
                left += 1
            else:
                right -= 1
        return res
    

        