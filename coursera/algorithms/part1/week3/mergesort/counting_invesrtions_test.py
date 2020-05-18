import unittest

from coursera.algorithms.part1.week3.mergesort.counting_inversions import CountingInversions


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ci = CountingInversions()
        a = [9, 8, 7, 6, 5]
        print(ci.count(a))


if __name__ == '__main__':
    unittest.main()
