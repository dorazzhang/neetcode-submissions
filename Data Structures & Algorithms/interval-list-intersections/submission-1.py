class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        # two lists of closed intervals
        # [start, end]
        # each list is pairwise disjoint and in sorted order

        # return intersection of the two lists

        # two intervals intersect when start time of later finishing interval is less than finish time of the earlier finishing interval 
        # [1, 5] | [2, 4] [5,6]
        # [1, 3] [4, 5] # [5, 5]

        # two pointer approach
        # for every pair, identify which finishes earlier and later
        # if start later <= finish earlier, then append [s, f] and increment both pointers
        # otherwise if they dont overlap, increment the pointer that has the earlier finish time

        # stop when either list is empty

        p1 = 0
        p2 = 0
        res = []

        if not firstList or not secondList:
            return []
        
        while p1 < len(firstList) and p2 < len(secondList):
            s = max(firstList[p1][0], secondList[p2][0])
            f1 = firstList[p1][1]
            f2 = secondList[p2][1]
            f = min(f1, f2)

            if s <= f:
                res.append([s, f])
            if f1 >= f2:
                p2 += 1
            if f2 >= f1:
                p1 += 1
        
        return res
