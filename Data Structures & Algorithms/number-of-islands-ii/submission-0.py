class UnionFind:
    def __init__(self, size):
        self.parent = [-1] * size
        self.rank = [0] * size
        self.count = 0
    def find(self, x):
        p = self.parent[x]
        while p != self.parent[p]:
            self.parent[p] = self.parent[self.parent[p]]
            p = self.parent[p]
        return p
    def union(self, x, y):
        xp = self.find(x)
        yp = self.find(y)

        if xp == yp:
            return False
        elif self.rank[xp] < self.rank[yp]:
            self.parent[xp] = yp
        elif self.rank[xp] > self.rank[yp]:
            self.parent[yp] = xp
        else:
            self.parent[yp] = xp
            self.rank[xp] += 1

        self.count -= 1
    def add_land(self, x):
        if self.parent[x] >= 0:
            return
        self.parent[x] = x
        self.count += 1
    def is_land(self, x):
        if self.parent[x] >= 0:
            return True
        else:
            return False

    def number_of_islands(self):
        return self.count

class Solution:
    def numIslands2(self, m: int, n: int, positions: List[List[int]]) -> List[int]:
        # initially all water cells
        # position[i] = r, c where we operate the ith operation
        # return array of island count after every operation 
        # every operation is adding one land at a time
        # is another island if surrounded by water, else it forms the same island
        # can u not just have a dictionary storing land cells
        # and for every new operation, check if up down right left cells r alr in dictionary (if it is, dont increment island count)

        # time complexity: O(k)

        # nope, bc sometimes a piece of land might connect two island into one, and you wouldnt know

        # union find

        x = [-1, 1, 0, 0]
        y = [0, 0, -1, 1]

        dsu = UnionFind(m * n)
        answer = []

        for pos in positions:
            land_pos = pos[0] * n + pos[1]
            dsu.add_land(land_pos)

            for i in range(4):
                neighbor_x = pos[0] + x[i]
                neighbor_y = pos[1] + y[i]
                neighbor_pos = neighbor_x * n + neighbor_y

                if neighbor_x >= 0 and neighbor_x < m and neighbor_y >= 0 and neighbor_y < n and dsu.is_land(neighbor_pos):
                    dsu.union(land_pos, neighbor_pos)
            
            answer.append(dsu.number_of_islands())
        
        return answer
