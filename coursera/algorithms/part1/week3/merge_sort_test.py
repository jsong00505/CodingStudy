import random
import unittest

from coursera.algorithms.part1.week3.merge_sort import MergeSort


class MyTestCase(unittest.TestCase):
    def test_something(self):

        ms = MergeSort()
        a = [9,8,7,6,5,4,3]
        print(ms.sort(a))



if __name__ == '__main__':
    unittest.main()
