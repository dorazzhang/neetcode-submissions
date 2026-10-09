class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        word = False
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " " and word:
                break
            if s[i] != " " and not word:
                word = True
                count += 1
            elif s[i] != " " and word:
                count += 1
        return count