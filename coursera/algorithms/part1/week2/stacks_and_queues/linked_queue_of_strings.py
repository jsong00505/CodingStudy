from util.node import Node


class LinkedQueueOfStrings:
    def __init__(self):
        self.first = None
        self.last = None

    def enqueue(self, item):
        old_last = self.last
        self.last = Node(item)
        if self.is_empty():
            self.first = self.last
        else:
            old_last.next = self.last

    def dequeue(self):
        item = self.first.item
        self.first = self.first.next
        if self.is_empty():
            self.last = None
        return item

    def is_empty(self):
        return not self.first