class Solution:
    def countSubstrings(self, s: str) -> int:

        # let dp[i][j] be if substring s[i...j] is a palindrome

        res = 0
        # 2d dp array storing whether a substring is a palindrome
        dp = [[False] * len(s) for _ in range(len(s))]
        # loop starting with i pointer at the end
        # loop would look like "c" "b" "bc" "a" "ab" "abc" for string "abc". at abc, it checks if a == c and the substring in between is a palindrome, which was already calculated prior
        for i in range(len(s) - 1, -1, -1):
            # j = i first and increments
            for j in range(i, len(s)):
                if s[i] == s[j] and (j - i <= 2 or dp[i + 1][j - 1]):
                    dp[i][j] = True
                    res += 1
        return res