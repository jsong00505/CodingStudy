class LinkedStackOfStrings:
    class Node:
        def __init__(self, item):
            self.item = item
            self.next = None

    first = None

    def is_empty(self):
        return not self.first

    def push(self, item):
        first = self.first
        old_first = first
        first = self.Node(item)
        first.next = old_first

    def pop(self):
        first = self.first
        item = first.item
        first = first.next
        return item
