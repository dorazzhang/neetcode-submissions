class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        # unqiue palindromes of length 3
        # subsequence of s
        
        # "aabca"
        # "bbcbaba"
        # characteristic of a length 3 palindrome -> the two numbers on the sides are the same, and the middle character can be anything
            # just looking for pairs of the same letter
        
        # "bbcbaba"
        # "b    b"
        # " b b  " <- can ignore these because the characters available to you in the middle were alr available to the earlier pair and we want uniqueness
        # "    a a"

        # two pointers, and we fix one of them until we get a pair or exhaust our search
        # keep record of side characters that we've alr used, skip if seen again
        # once we find a pair, we continue advancing over pointer but this time for the middle character and add the palindromes to a set

        res = set()

        #since we only care about unique characters, we use a set for possible side characters
        for ch in set(s):
            left = s.find(ch) # finds index of first occurance of ch in s
            right = s.rfind(ch) # finds index of last occurance of ch in s
            # -1 if not found
            if right - left >= 2: # only one occurence, r-l = 0, 0 occurences, r-l = -2
                for mid in set(s[left + 1:right]):
                    res.add(ch + mid + ch)

        return len(res)