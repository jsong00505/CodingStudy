class StackWithMax:
    def __init__(self):
        self.stack = []
        self.m = []

    def push(self, item):
        self.stack.append(item)
        if not self.m or (self.m and item > self.m[-1]):
            self.m.append(item)

    def pop(self):
        item = self.stack.pop()
        if self.m and item == self.m[-1]:
            self.m.pop()
        return item

    def get_max(self):
        item = self.m[-1]
        return item
