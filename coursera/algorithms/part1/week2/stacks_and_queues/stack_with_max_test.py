import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.stack_with_max import StackWithMax


class MyTestCase(unittest.TestCase):
    def test_something(self):
        stack = StackWithMax()
        stack.push(1)
        print("push 1")
        print("max: %d" % stack.get_max())
        stack.push(2)
        print("push 2")
        print("max: %d" % stack.get_max())
        stack.push(-1)
        print("push -1")
        print("max: %d" % stack.get_max())
        print("pop: %d" % stack.pop() )
        print("max: %d" % stack.get_max())
        print("pop: %d" % stack.pop())
        print("max: %d" % stack.get_max())




if __name__ == '__main__':
    unittest.main()
