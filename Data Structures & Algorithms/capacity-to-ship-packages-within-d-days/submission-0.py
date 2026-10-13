class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        # packages that must be shipped from one to the other within x days
        # ith package has weight weights[i]
        # not allowed to load more than max weight in a day
        # least weight capacity of ship that allows packages to be shipped within _ days

        # [2,4,6,1,3,10]
        # 4

        # way to split into four groups while minimizing sum

        # im dumb i didnt see it said in the order given by weights
        # 2 groups of 2
        # 2 groups of 1

        # try different capacities starting from first index?
        # binary search on the capacities themselves

        # [max(weights), sum(weights)]

        def canShip(capacity):
            # add as many items as you can to each ship that doesnt exceed capacity
            # when it does exceed, start a new ship to add it to
            ships = 1
            curr = capacity
            for w in weights:
                if curr - w < 0:
                    ships += 1
                    if ships > days:
                        return False
                    curr = capacity
                curr -= w
            return True
        
        l = max(weights)
        r = sum(weights)
        res = sum(weights)
        while l <= r:
            mid = (l + r) // 2
            if canShip(mid):
                res = min(res, mid)
                r = mid - 1
            else:
                l = mid + 1
        
        return res
            