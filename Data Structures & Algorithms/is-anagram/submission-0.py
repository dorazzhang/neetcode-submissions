class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        # can just sort both and see if they're equal, but that is a
        # special privledge of having that function avail

        count = [0] * 26 # array of 26 values
        for i in range(len(s)):
            count[ord(s[i]) - ord('a')] += 1
            count[ord(t[i]) - ord('a')] -= 1
        for num in count:
            if num != 0:
                return False
        return True
        