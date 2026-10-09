class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # need to keep track of seen numbers, unique only
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False
        