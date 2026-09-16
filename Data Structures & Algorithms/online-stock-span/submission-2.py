class StockSpanner:

    def __init__(self):
        self.stack = [] #[price, length]

    def next(self, price: int) -> int:
        length = 1

        while self.stack and self.stack[-1][0] <= price:
            length += self.stack[-1][1]
            self.stack.pop()
        self.stack.append([price, length])
        return length

# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)