import unittest

from coursera.algorithms.part1.week2.stacks_and_queues.permutation import Permutation


class MyTestCase(unittest.TestCase):
    def test_permutation_1(self):
        p = Permutation(3, "A B C D E F G H I")
        p.permutation()
        print()

    def test_permutation_2(self):
        p = Permutation(8, "AA BB BB BB BB BB CC CC")
        p.permutation()

if __name__ == '__main__':
    unittest.main()
