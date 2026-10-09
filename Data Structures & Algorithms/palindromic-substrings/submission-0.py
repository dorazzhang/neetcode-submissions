class Solution:
    def countSubstrings(self, s: str) -> int:

        # let dp[i][j] be if substring s[i...j] is a palindrome

        res = 0
        dp = [[False] * len(s) for _ in range(len(s))]

        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res