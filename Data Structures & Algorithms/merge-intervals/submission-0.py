class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        
        intervals.sort()
        res = [intervals[0]]

        for s1, f1 in intervals:
            f2 = res[-1][1]
            if s1 <= f2:
                res[-1][1] = max(f1, f2)
            else:
                res.append([s1, f1])
        return res
            
        