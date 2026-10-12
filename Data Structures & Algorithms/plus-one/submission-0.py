class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 0
        res = []
        i = len(digits) - 1

        while i >= 0 or carry != 0:
            add = 0
            if i == len(digits) - 1:
                add = 1
            if i >= 0:
                total = digits[i] + add + carry
            else:
                total = add + carry
            res.append(total % 10)
            carry = total // 10
            i -= 1
        
        res.reverse()
        return res