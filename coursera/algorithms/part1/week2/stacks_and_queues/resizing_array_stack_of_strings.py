class ResizingArrayStackOfStrings:

    def __init__(self):
        self.s = [None]
        self.n = 0

    def push(self, item):
        if self.n == len(self.s):
            self.resize(self.n * 2)
        self.s[self.n] = item
        self.n += 1

    def pop(self):
        self.n -= 1
        item = self.s[self.n]
        if self.n > 0 and self.n == len(self.s) // 4:
            self.resize(len(self.s) // 2)
        return item

    def resize(self, capacity: int):
        r = capacity - len(self.s)

        if r > 0:
            for i in range(r):
                self.s.append(None)
        else:
            for i in range(r * (-1)):
                self.s.pop()
