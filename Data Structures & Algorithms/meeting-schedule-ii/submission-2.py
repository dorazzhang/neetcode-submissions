"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0
        count = 1
        rooms = []
        heapq.heappush(rooms, intervals[0].end)
        intervals.sort(key = lambda interval: interval.start)
        for i in range(1, len(intervals)):
            if intervals[i].start < intervals[i - 1].end:
                if rooms[0] <= intervals[i].start:
                    heapq.heappop(rooms)
                else:
                    count += 1
                heapq.heappush(rooms, intervals[i].end)
        return count