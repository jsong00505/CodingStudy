import math
import random
import timeit
import unittest

from coursera.algorithms.part1.week1.analysis_of_algorithms.three_sum import ThreeSum


class MyTestCase(unittest.TestCase):
    def test_brute_force(self):
        ts = ThreeSum()

        for i in range(3):
            n = int(math.pow(2, i) * 100)
            a = [random.randint(-1000, 1000) for i in range(n)]
            start = timeit.default_timer()
            ans = ts.brute_force(a)
            stop = timeit.default_timer()
            print("Running Time(%d): %f " % (n, (stop - start)))

    def test_sorting_based(self):
        ts = ThreeSum()
        a = [30, -40, -20, -10, 40, 0, 10, 5]
        expected = 4
        actual = ts.sorting_based(a)

        self.assertEqual(expected, actual)

    def test_hashing_based(self):
        ts = ThreeSum()
        a = [30, -40, -20, -10, 40, 0, 10, 5]
        expected = 4
        actual = ts.hasing_based(a)

        self.assertEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
