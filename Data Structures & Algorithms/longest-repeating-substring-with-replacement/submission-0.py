class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # sliding window with i and j starting at 0
        # while i and j < length
        # check diff of tot length - count of most freq char in substring i-j
        # if its less than or equal than k, increment res and increment j
        # if its greater, increment i until its not, decrementing res
        # if not s:
        #     return 0
        # i = 0
        # j = 0
        # length = 0
        # res = 0
        # count = defaultdict(int)
        # while i < len(s) and j < len(s):
        #     if (j - i - max(count.values())) <= k:
        #         count[s[j]] += 1
        #         length += 1
        #         res = max(length, res)
        #         j += 1
        #     else:
        #         count[s[i]] -= 1
        #         i += 1
        #         length -= 1
        # return res

        l = 0
        res = 0
        length = 0
        count = defaultdict(int)
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res
            
        
            
            




        