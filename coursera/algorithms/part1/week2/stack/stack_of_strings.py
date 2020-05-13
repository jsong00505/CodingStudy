class StackOfStrings:
    def __init__(self):
        self.stack = []

    def push(self, item: str):
        self.stack.append(item)

    def pop(self):
        return self.stack.pop()

    def is_empty(self):
        return not self.stack
