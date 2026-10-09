class Solution:

    def __init__(self, w: List[int]):
        self.prefix_sum = [0]
        for weight in w:
            self.prefix_sum.append(self.prefix_sum[-1] + weight)

    def pickIndex(self) -> int:
        target = self.prefix_sum[-1] * random.random()
        L, R = 1, len(self.prefix_sum)
        while L < R:
            mid = (L + R) // 2
            if self.prefix_sum[mid] <= target:
                L = mid + 1
            else:
                R = mid
        return L - 1


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()