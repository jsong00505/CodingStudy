from coursera.algorithms.part1.week2.stacks_and_queues.iterator import Iterator


class Deque:

    # construct an empty deque
    def __init__(self):
        self.deque = []

    # is the deque empty?
    def is_empty(self):
        return not self.deque

    # return the number of items on the deque
    def size(self):
        return len(self.deque)

    # add the item to the front
    def add_first(self, item):
        if item == None:
            raise ValueError
        self.deque.insert(0, item)

    # add the item to the back
    def add_last(self, item):
        if item == None:
            raise ValueError
        self.deque.append(item)

    # remove and return the item from the front
    def remove_first(self):
        if self.is_empty():
            raise UnboundLocalError
        return self.deque.pop(0)

    # remove and return the item from the back
    def remove_last(self):
        if self.is_empty():
            raise UnboundLocalError
        return self.deque.pop()

    def iterator(self):
        return Iterator(self.deque)
