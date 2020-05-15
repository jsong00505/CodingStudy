import random
import unittest

from coursera.algorithms.part1.week2.elementary_sorts.dutch_national_flag import DutchNationalFlag


class MyTestCase(unittest.TestCase):
    def test_something(self):
        dnf = DutchNationalFlag(self.gen_buckets(20))
        dnf.sort()

    def gen_buckets(self, n):
        pebbles = ['R', 'W', 'B']
        buckets = []
        for i in range(n):
            buckets.append(pebbles[random.randint(0, 2)])
        return buckets



if __name__ == '__main__':
    unittest.main()
