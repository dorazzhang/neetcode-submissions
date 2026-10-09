class Solution:
    # input: string s, output: substring s
    def longestPalindrome(self, s: str) -> str:
        # palindromes expand from the center
        # check every index by making it the center of a palidrome
        resIdx = 0
        resLen = 0
        for i in range(len(s)):
            # for each center, it is either an even or odd palidrome

            l = i
            r = i
            length = 1
            while l >= 0 and r < len(s) and s[l] == s[r]:
                if r != i:
                    length += 2
                l -= 1
                r += 1
            resLen = max(resLen, length)
            if resLen == length:
                resIdx = l + 1

            l = i
            r = i + 1
            length = 0
            while l >= 0 and r < len(s) and s[l] == s[r]:
                length += 2
                l -= 1
                r += 1
            resLen = max(resLen, length) 
            if resLen == length:
                resIdx = l + 1
        
        return s[resIdx:resIdx+resLen]

                    
        