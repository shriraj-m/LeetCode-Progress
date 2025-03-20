"""Online Stock Span"""

class StockSpanner:

    def __init__(self):
        self.stack = []

    def next(self, price: int) -> int:
        span = 1
        last_span = 0
        # check if price is >= the top of the stack's price. 
        while self.stack and price >= self.stack[-1][0]:
            _, last_span = self.stack.pop() # we also get span of most recent.
            span += last_span # add the span of the previous
        self.stack.append((price,span)) # we now have span for current price.
        return span

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)