import unittest

from coursera.algorithms.part1.week3.mergesort.bottom_up_mergesort import BottomUpMergesort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bums = BottomUpMergesort()
        a = [9, 8, 7, 6, 5, 4, 3]
        print(bums.sort(a))


if __name__ == '__main__':
    unittest.main()
