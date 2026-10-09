class Solution:
    def maxArea(self, heights: List[int]) -> int:
        # two pointer, move pointer with shorter height
        # min(heights[i], heights[j]) * (j - i)
        i = 0
        j = len(heights) - 1
        ans = min(heights[i], heights[j]) * (j - i)
        while i < j:
            area = min(heights[i], heights[j]) * (j - i)
            if area > ans:
                ans = area
            if heights[i] <= heights[j]:
                i += 1
            else:
                j -= 1
        return ans


        