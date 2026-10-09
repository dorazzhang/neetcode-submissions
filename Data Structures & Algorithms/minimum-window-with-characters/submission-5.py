class Solution:
    def minWindow(self, s: str, t: str) -> str:
        l = 0
        res = ""
        length = ""
        count = defaultdict(int)
        for c in t:
            count[c] += 1
        seen = defaultdict(int)
        have = 0
        need = len(count)

        for r in range(len(s)):
            seen[s[r]] += 1
            if s[r] in count and seen[s[r]] == count[s[r]]:
                have += 1
            while l < len(s) and (seen[s[l]] > count[s[l]] or count[s[l]] == 0):
                if s[l] in count and seen[s[l]] == count[s[l]]:
                    have -= 1
                seen[s[l]] -= 1
                l += 1
            if have == need:
                length = s[l:r + 1]
            if not res or len(length) < len(res):
                    res = length
        return res
            

                
