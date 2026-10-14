class Solution:
    def reverse(self, x: int) -> int:
        negative = False
        if x < 0:
            negative = True
            x *= -1
        x_reversed = 0

        while x > 0:
            x_reversed = (x_reversed * 10) + (x % 10)
            x //= 10
        
        if negative:
            x_reversed *= -1
        return x_reversed if -2**31 <= x_reversed <= 2**31 - 1 else 0
        