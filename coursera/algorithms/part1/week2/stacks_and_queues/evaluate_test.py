import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.evaluate import Evaluate


class MyTestCase(unittest.TestCase):
    def test_something(self):
        s = "( 1 + ( ( 2 + 3 ) * ( 4 * 5 ) ) )"
        e = Evaluate()
        expected = 101
        actual = e.evaluate(s)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
