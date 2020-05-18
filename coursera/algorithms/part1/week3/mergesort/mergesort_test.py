import unittest

from coursera.algorithms.part1.week3.mergesort.mergesort import Mergesort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ms = Mergesort()
        a = [9, 8, 7, 6, 5, 4, 3]
        print(ms.sort(a))


if __name__ == '__main__':
    unittest.main()
