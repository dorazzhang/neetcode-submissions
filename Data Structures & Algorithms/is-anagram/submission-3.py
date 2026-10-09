class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # sort and compare
        # return sorted(s) == sorted(t)

        # if you can't sort, create count hashMap?

        # countS = defaultdict() # key is character, value is count
        # countT = defaultdict()
        # for char in s:
        #     if char in countS:
        #         countS[char] += 1
        #     else:
        #         countS[char] = 0
        # for char in t:
        #     if char in countT:
        #         countT[char] += 1
        #     else:
        #         countT[char] = 0
        # return countS == countT

        # less lines of code

        countS = defaultdict(int) # key is character, value is count
        countT = defaultdict(int)
        if len(s) != len(t):
            return False
        for i in range(len(s)):
            countS[s[i]] += 1
            countT[t[i]] += 1
        return countS == countT

        