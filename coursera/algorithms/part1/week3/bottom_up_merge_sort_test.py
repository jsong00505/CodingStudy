import unittest

from coursera.algorithms.part1.week3.bottom_up_merge_sort import BottomUpMergeSort


class MyTestCase(unittest.TestCase):
    def test_something(self):
        bums = BottomUpMergeSort()
        a = [9, 8, 7, 6, 5, 4, 3]
        print(bums.sort(a))


if __name__ == '__main__':
    unittest.main()
