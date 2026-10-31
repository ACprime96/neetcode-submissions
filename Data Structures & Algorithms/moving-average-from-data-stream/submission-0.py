class MovingAverage:

    def __init__(self, size: int):
        self.window = deque()
        self.max_size = size
        self.cur_sum = 0

    def next(self, val: int) -> float:
        if len(self.window) == self.max_size:
            self.cur_sum -= self.window.popleft()
        
        self.window.append(val)
        self.cur_sum += val

        return self.cur_sum / len(self.window)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
