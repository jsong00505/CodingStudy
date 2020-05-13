import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.stack_of_strings import StackOfStrings


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = "to be or not to - be - - that - - - is"
        stack = StackOfStrings()
        words = s.split(' ')
        res = []
        for word in words:
            if word == '-':
                res.append(stack.pop())
            else:
                stack.push(word)
        print(" ".join(res))


if __name__ == '__main__':
    unittest.main()
