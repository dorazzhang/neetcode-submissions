class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum = ""

        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                maximum = max(maximum, num[i])

        return maximum * 3