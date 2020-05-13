import math
import random
import timeit
import unittest

from coursera.algorithms.part1.week1.analysis_of_algorithms.bitonic_array_search import BitonicArraySearch
from coursera.algorithms.part1.week1.analysis_of_algorithms.three_sum import ThreeSum


class MyTestCase(unittest.TestCase):
    def test_bitonic_array_search_1(self):

        bas = BitonicArraySearch()
        a = self.generate_bitonic_array(10)

        expected = random.randint(0, len(a) - 1)
        target = a[expected]
        actual = bas.search(a, target)
        self.assertEqual(expected, actual)

    def test_bitonic_array_search_2(self):
        bas = BitonicArraySearch()
        a = self.generate_bitonic_array(10)

        target = -1000
        expected = -1
        actual = bas.search(a, target)
        self.assertEqual(expected, actual)

    def generate_bitonic_array(self, n):
        point = random.randint(1, n - 2)
        num = random.randint(-10, 10)
        a = [num]
        while len(a) < n:
            add = random.randint(1, 10)
            if point > len(a) - 1:
                num = num + add
            else:
                num = num - add
                if num in a:
                    continue
            a.append(num)

        return a


if __name__ == '__main__':
    unittest.main()
