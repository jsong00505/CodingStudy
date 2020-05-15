import random
import unittest

from coursera.algorithms.part1.week2.elementary_sorts.intersection_of_two_sets import IntersectionOfTwoSets
from coursera.algorithms.part1.week2.elementary_sorts.point_2d import Point2D


class MyTestCase(unittest.TestCase):
    def test_something(self):

        its = IntersectionOfTwoSets()
        a = (self.gen_point_2d() for i in range(50))
        b = (self.gen_point_2d() for i in range(50))
        print(its.intersection(a, b))

    def gen_point_2d(self):
        return Point2D(random.randint(-5, 5), random.randint(-5, 5))



if __name__ == '__main__':
    unittest.main()
