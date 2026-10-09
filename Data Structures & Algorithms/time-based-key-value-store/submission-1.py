class TimeMap:

    def __init__(self):
        # hash map with list as value
        # index of list = time t
        self.hashmap = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # timestamp is strictly increasing so the resulting list is sorted in asc order
        if key not in self.hashmap:
            self.hashmap[key] = [(timestamp, value)]
        else:
            self.hashmap[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        #nlogn binary search

        if key not in self.hashmap:
            return ""
        
        values = self.hashmap[key]

        # binary search to get largest time <= timestamp

        L = 0
        R = len(values) - 1
        res = (-1, None)
        while L <= R:
            mid = (L + R) // 2
            if values[mid][0] == timestamp:
                return values[mid][1]
            elif values[mid][0] > timestamp:
                R = mid - 1
            else:
                if res[0] < values[mid][0]:
                    res = values[mid]
                L = mid + 1
        
        return "" if res[0] == -1 else res[1]
