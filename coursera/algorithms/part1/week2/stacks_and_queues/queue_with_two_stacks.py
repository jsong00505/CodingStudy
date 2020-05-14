class QueueWithTwoStacks:
    def __init__(self):
        self.stack = []

    def enqueue(self, item):
        self.stack.append(item)

    def dequeue(self):
        queue = []
        while self.stack:
            queue.append(self.stack.pop())
        item = queue.pop()
        while queue:
            self.stack.append(queue.pop())
        return item

    def is_empty(self):
        return not self.stack
