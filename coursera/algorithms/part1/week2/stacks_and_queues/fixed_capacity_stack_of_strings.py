class FixedCapacityStackOfStrings:

    def __init__(self, capacity: int):
        self.s = [None for i in range(capacity)]
        self.n = 0

    def is_empty(self):
        return self.n == 0

    def push(self, item):
        self.s[self.n] = item
        self.n += 1

    def pop(self):
        self.n -= 1
        return self.s[self.n]
