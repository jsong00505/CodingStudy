import random
import unittest

from coursera.algorithms.part1.week1.analysis_of_algorithms.binary_search import BinarySearch


class MyTestCase(unittest.TestCase):
    def test_binary_search_1(self):
        n = random.randint(100, 1000)
        l = [i for i in range(n)]
        target = random.randint(0, n)
        expected = target

        bs = BinarySearch()
        actual = bs.search(l, target)
        self.assertEqual(expected, actual)

    def test_binary_search_2(self):
        n = random.randint(100, 1000)
        l = [i for i in range(n)]
        target = random.randint(0, n) + 1000
        expected = -1

        bs = BinarySearch()
        actual = bs.search(l, target)
        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
