class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        perm = defaultdict(int)
        seen = defaultdict(int)
        for c in s1:
            perm[c] += 1
        l = 0
        for r in range(len(s2)):
            seen[s2[r]] += 1
            while (perm[s2[r]] - seen[s2[r]])  < 0:
                seen[s2[l]] -= 1
                l += 1
            if (r - l + 1) == len(s1):
                return True
        return False
        