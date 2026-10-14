class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # right shift: replace every letter with next letter in alpha (cyclic so z -> a)
        # left shift: replace every letter with preceding letter in alpha (a -> z)
        # valid inputs (strings with lowercase letters)
        
        # strings of length 1 are automatically in the same shifting sequence
        # same sequence of characters in string are same distance apart
        # mod 26
        # a : 0, z : 25 ord(c) - 'a' 0

        # az is 25 apart, ba is also 25 apart (b = 1, a = 26 or 0)
        # 26 + 'a'

        # yza : 24 25 0 -> 1 and -25 away from 24, % 26 -> 1 and 1 
        # xyz : 23 24 25

        shift_seq = defaultdict(list)

        for s in strings:
            distances = tuple(((ord(c) - ord(s[0])) % 26 for c in s))
            shift_seq[distances].append(s)
        
        return [lists for lists in shift_seq.values()]



