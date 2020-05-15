import unittest

from coursera.algorithms.part1.week2.elementary_sorts.permutation import Permutation


class MyTestCase(unittest.TestCase):
    def test_something(self):
        p = Permutation()
        a = [1,2,3,4]
        b = [1,2]
        print(p.permutation(a, b))
        print(p)


if __name__ == '__main__':
    unittest.main()
