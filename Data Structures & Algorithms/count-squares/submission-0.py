class CountSquares:
    # from one point (x, y), need another point with same x (x, y1) and another with same y (x2, y)
    # last point has to be (x2, y1)

    # or see that the diagonal has to be the same x and y distance away
    # from there, the sides can be found from the diagonal and og point

    def __init__(self):
        # hashmap of points and their freqs
        self.pointsCount = defaultdict(int)
        self.points = []

    def add(self, point: List[int]) -> None:
        self.pointsCount[tuple(point)] += 1
        self.points.append(point)

    def count(self, point: List[int]) -> int:
        res = 0
        px, py = point
        for x, y in self.points:
            if (abs(py - y) != abs(px - x)) or x == px or y == py:
                continue
            
            res += self.pointsCount[(x, py)] * self.pointsCount[(px, y)]
        
        return res