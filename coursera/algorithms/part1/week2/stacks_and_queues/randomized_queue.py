import random

from coursera.algorithms.part1.week2.stacks_and_queues.iterator import Iterator


class RandomizedQueue:

    # construct an empty randomized queue
    def __init__(self):
        self.queue = []

    # is the randomized queue empty?
    def is_empty(self):
        return not self.queue

    # return the number of items on the randomized queue
    def size(self):
        return len(self.queue)

    # add the item
    def enqueue(self, item):
        if not item:
            raise ValueError
        self.queue.append(item)

    # remove and return a random item
    def dequeue(self):
        if self.is_empty():
            raise UnboundLocalError
        self.queue.pop(self.get_rand())

    # return a random item (but do not remove it)
    def sample(self):
        if self.is_empty():
            raise UnboundLocalError
        return self.queue[self.get_rand()]

    def get_rand(self):
        return random.randint(0, len(self.queue) - 1)

    def iterator(self):
        return RandomizedIterator(self.queue)


class RandomizedIterator:

    def __init__(self, l):
        self.i = l.copy()

    def next(self):
        if not self.i:
            raise UnboundLocalError
        item = self.i.pop(self.get_rand())
        return item

    def has_next(self):
        return self.i

    def remove(self):
        raise AttributeError

    def get_rand(self):
        return random.randint(0, len(self.i) - 1)
