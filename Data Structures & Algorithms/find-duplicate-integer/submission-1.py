class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        # nums with n + 1 integers
        # [1, n]

        # there's one repeated integer in nums, find that integer

        # can just use a set and return when integer in set, O(n) space, O(n) time

        # without modifying array and no extra space...

        # pretend the array is a linked list where the value is the index its point to

        # if you use fast and slow pointers where they overlap at some point, that means values are the same

        slow = 0
        fast = 0

        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]

            if slow == fast:
                break
        
        slow2 = 0

        while True:
            slow2 = nums[slow2]
            slow = nums[slow]
            if slow == slow2:
                return slow