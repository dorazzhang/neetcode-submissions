class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        # at every position, you either delete or keep the element
        # but no because once you go to another element, you might have to delete a previous one

        # recursion to go down every branch of either including or not including a value, only valid if the curr elem is greater than previous

        # 2^n possible subsequences

        #can use cache to make O(n^2)

        # start at last index and work backwards where dp[i] is max length starting at index i
        dp = [1] * len(nums)
        for i in range(len(nums) - 2, -1, -1):
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    dp[i] = max(dp[i], 1 + dp[j])

        return max(dp)
        