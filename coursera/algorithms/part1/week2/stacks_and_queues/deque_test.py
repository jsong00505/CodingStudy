import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.deque import Deque


class MyTestCase(unittest.TestCase):
    def test_something(self):
        deque = Deque()
        deque.add_first(1)
        deque.add_last(2)
        deque.add_first(3)
        deque.add_last(4)
        deque.add_first(5)
        deque.add_last(6)

        i = deque.iterator()
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

        deque.iterator()
        deque.remove_first()
        deque.remove_first()
        deque.remove_first()
        deque.remove_last()
        deque.remove_last()
        deque.remove_last()
        try:
            deque.remove_first()
        except UnboundLocalError:
            print("expected")
        try:
            deque.remove_last()
        except UnboundLocalError:
            print("expected")


if __name__ == '__main__':
    unittest.main()
