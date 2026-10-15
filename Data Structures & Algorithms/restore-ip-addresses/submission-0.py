class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        
# 4 integers separated by "."
# each is between 0 and 255, no leading zeros
# given string s containing only digits
# all possible IP addresses that can be formed

# 101023
# 1.0.10.23 
# 1.01.0.23 -> no leading zeros
# you need a number between 0-255 to go before/after 3 periods


# iterative approach, first decide the first group of numbers, then run again for the next group

# at every group, either slice one digit, two digits, or three digits

# 1 dfs("1.", 1, 1) # res and index and which group we're building
# 10 -> dfs(10, 0, 0)
# 101 -> dfs(101, 0, 0)

# once we build all 4 groups, we can return

        res = []

        if len(s) > 12:
            return res

        def backtrack(string, index, dots):
            nonlocal res
            if dots == 4 and index == len(s):
                res.append(string[:-1])
            if dots > 4:
                return
            for j in range(index, min(index + 3, len(s))):
                if int(s[index:j+1]) < 256 and (index == j or s[index] != '0'):
                    backtrack(string + s[index:j+1] + ".", j + 1, dots + 1)
        
        backtrack("", 0, 0)
        return res
