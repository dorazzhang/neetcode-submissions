class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        curr = nums[0]
        longest = 1
        count = 1
        sortedNums = sorted(nums)
        for num in sortedNums:
            if num == curr:
                continue
            if num == curr + 1:
                count += 1
            else:
                count = 1
            if count > longest:
                longest = count
            curr = num
        
        return longest
        