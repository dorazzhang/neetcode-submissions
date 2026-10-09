class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        # can create an array from left to right of distance balls have to travel, then other way and add them

        left = [0]
        total = 0
        count = 0
        # [0, 1, 3]
        # [0, 0, 0, 1, 2, ]
        for i in range(1, len(boxes)):
            total += count
            if boxes[i - 1] == "1":
                total += 1
                count += 1
            left.append(total)
        
        right = [0]
        total = 0
        count = 0

        for i in range(len(boxes) - 2, -1, -1):
            total += count
            if boxes[i + 1] == "1":
                total += 1
                count += 1
            right.append(total)
        
        right.reverse()

        res = []

        for i in range(len(boxes)):
            res.append(left[i] + right[i])
        
        return res


        