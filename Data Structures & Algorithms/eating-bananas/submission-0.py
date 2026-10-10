class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        # number of bananas in ith pile
        # number of hours to eat bananas

        # decide rate k (can only eat from one pile every hour)
        # minimum integer k such that you can eat all bananas within h hours

        # [1, 4, 3, 2] h = 9 
        # 10
        # if you have 4 hours, you would have to use the max in the array as your rate
        
        # max in the array is our upper bound

        # search for k from 1 to max

        # check if k is greater or less than needed

        left = 1
        right = max(piles)
        res = right

        while left <= right:
            mid = (left + right) // 2 # k = mid

            total_hours = 0
            for pile in piles:
                total_hours += math.ceil(pile / mid)
            
            if total_hours <= h:
                res = mid
                right = mid - 1
            else:
                left = mid + 1
        return res
