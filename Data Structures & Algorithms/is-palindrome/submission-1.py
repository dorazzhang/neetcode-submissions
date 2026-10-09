class Solution:
    def isPalindrome(self, s: str) -> bool:
        j = 0
        i = len(s) - 1
        while j < i:
            while j < i and not s[j].isalnum():
                j += 1
            while j < i and not s[i].isalnum():
                i -= 1
            if s[j].lower() != s[i].lower():
                return False
            j += 1
            i -= 1
        return True
        