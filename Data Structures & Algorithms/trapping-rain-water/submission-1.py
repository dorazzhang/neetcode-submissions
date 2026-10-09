class Solution:
    def trap(self, height: List[int]) -> int:
        maxLeft = []
        maxRight = []

        l = 0
        r = 0

        area = 0
        for h in height:
            maxLeft.append(l)
            l = max(l, h)

        for i in range(len(height) - 1, -1, -1):
            maxRight.append(r)
            r = max(r, height[i])

        maxRight.reverse()

        for i in range(len(height)):
            area += max(0, min(maxLeft[i], maxRight[i]) - height[i])
        return area

        


              