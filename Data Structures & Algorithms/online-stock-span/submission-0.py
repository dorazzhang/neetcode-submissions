class StockSpanner:

    # daily price quotes for some stock
    # span of stocks price
    # max number of consecutive days stock was <= curr day (including curr day so min span = 1)
    
    def __init__(self):
        self.stack = [] # stores (price, span)

    def next(self, price: int) -> int:
        span = 1
        while self.stack:
            if self.stack[-1][0] > price:
                break
            else:
                _, prev_span = self.stack.pop() 
                span += prev_span
        self.stack.append((price, span))
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)