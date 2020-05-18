import unittest

from coursera.algorithms.part1.week3.mergesort.merging_with_smaller_auxiliary_array import \
    MergingWithSmallerAuxiliaryArray


class MyTestCase(unittest.TestCase):
    def test_something(self):
        mwsaa = MergingWithSmallerAuxiliaryArray()
        a = [6, 7, 8, 9, 2, 3, 4, 5]
        print(mwsaa.sort(a, 4))


if __name__ == '__main__':
    unittest.main()
