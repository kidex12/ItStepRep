
class Counter:
    def __init__(self):
        self.count = 0
    def increment(self):
        self.count += 1
    def decrement(self):
        self.count -= 1
    def reset(self):
        self.count = 0

obj = Counter()
obj.increment()
obj.increment()
obj.decrement()
obj.reset()


