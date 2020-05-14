import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.deque import Deque
from coursera.algorithms.part1.week2.stacks_and_queues.randomized_queue import RandomizedQueue


class MyTestCase(unittest.TestCase):
    def test_something(self):
        queue = RandomizedQueue()
        queue.enqueue(1)
        queue.enqueue(2)
        queue.enqueue(3)
        queue.enqueue(4)
        queue.enqueue(5)
        queue.enqueue(6)

        i = queue.iterator()
        print(i.next())
        print(i.next())
        print(i.next())
        print(i.next())
        print(i.next())
        print(i.next())

        try:
            i.next()
        except UnboundLocalError:
            print("expected")

        try:
            i.remove()
        except AttributeError:
            print("expected")

        queue.iterator()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        queue.dequeue()
        try:
            queue.dequeue()
        except UnboundLocalError:
            print("expected")
        try:
            queue.dequeue()
        except UnboundLocalError:
            print("expected")


if __name__ == '__main__':
    unittest.main()
