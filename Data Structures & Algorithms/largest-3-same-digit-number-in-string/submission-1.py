class Solution:
    def largestGoodInteger(self, num: str) -> str:
        maximum = -1

        for i in range(2, len(num)):
            if num[i] == num[i - 1] == num[i - 2]:
                maximum = max(maximum, int(num[i]))

        return str(maximum) * 3 if maximum != -1 else ""