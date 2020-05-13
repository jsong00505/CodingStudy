import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.linked_queue_of_strings import LinkedQueueOfStrings


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = "to be or not to - be - - that - - - is"
        queue = LinkedQueueOfStrings()
        words = s.split(' ')
        res = []
        for word in words:
            if word == '-':
                res.append(queue.dequeue())
            else:
                queue.enqueue(word)
        print(" ".join(res))


if __name__ == '__main__':
    unittest.main()
