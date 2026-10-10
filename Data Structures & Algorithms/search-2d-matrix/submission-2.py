class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # each row is sorted
        # whole matrix is sorted essentially

        # ith element in list given r, c?
        # 0,0 = 0*4 + 0 + 1st
        # 1,0 = 1*4 + 0 + 1
        # other way, 5 % 4 = 1 - 1 -> 1,0
        # math.ceil(5 // 4) = 2 - 1

        # find target in matrix

        left = 1 
        right = len(matrix[0]) * len(matrix)
        COLS = len(matrix[0])

        while left <= right:
            mid = (left + right) // 2

            left_r = math.ceil(left / COLS) - 1
            left_c = ((left - 1) % COLS)

            right_r = math.ceil(right / COLS) - 1
            right_c = ((right - 1) % COLS)

            mid_r = math.ceil(mid / COLS) - 1
            mid_c = ((mid - 1) % COLS)

            if matrix[mid_r][mid_c] == target:
                return True
            elif matrix[mid_r][mid_c] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False