class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # total = 1
        # zcount = 0
        # for num in nums:
        #     if num == 0:
        #         zcount += 1
        # if zcount > 1: return [0] * len(nums)

        # for i, num in enumerate(nums):
        #     if num:
        #         total *= num
        # result = []
        # for num in nums:
        #     if zcount:
        #         if num:
        #             result.append(0)
        #         else:
        #             result.append(total)
        #     else:
        #         result.append(total//num)
        # return result
            
        prefix = 1
        result = [1] * len(nums)

        for i, num in enumerate(nums):
            result[i] *= prefix
            prefix *= num
        
        postfix = 1
        for i in range(len(nums) - 1, -1, -1):
            result[i] *= postfix
            postfix *= nums[i]
        return result
