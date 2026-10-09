class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        sub_set = set()
        l = 0
        length = 0
        for i in range(len(s)):
            while s[i] in sub_set:
                sub_set.remove(s[l])
                l += 1
            sub_set.add(s[i])
            length = max(length, len(sub_set))
        return length
            
            
            
        

        