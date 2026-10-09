class Solution:
    def isPalindrome(self, s: str) -> bool:
        s_lower = s.lower()
        j = 0
        i = len(s) - 1
        while j < i:
            while j < i and not s_lower[j].isalnum():
                j += 1
            while j < i and not s_lower[i].isalnum():
                i -= 1
            if s_lower[j] != s_lower[i]:
                return False
            j += 1
            i -= 1
        return True
        