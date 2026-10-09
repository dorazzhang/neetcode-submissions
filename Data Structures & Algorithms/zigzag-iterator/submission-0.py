class ZigzagIterator:
    def __init__(self, v1: List[int], v2: List[int]):
        self.vectors = [v1, v2]
        self.queue = deque()

        if v1: 
            self.queue.append((0, 0))
        if v2:
            self.queue.append((1,0))

    def next(self) -> int:
        if self.queue:
            vec_index, elem_index  = self.queue.popleft()
            if elem_index + 1 < len(self.vectors[vec_index]):
                self.queue.append((vec_index, elem_index + 1))
        
        return self.vectors[vec_index][elem_index]

    def hasNext(self) -> bool:
        if self.queue:
            return True
        else:
            return False

        

# Your ZigzagIterator object will be instantiated and called as such:
# i, v = ZigzagIterator(v1, v2), []
# while i.hasNext(): v.append(i.next())
