from typing import List, Set

from coursera.algorithms.part1.week2.elementary_sorts.point_2d import Point2D


class IntersectionOfTwoSets:
    def intersection(self, a: Set[Point2D], b: Set[Point2D]):

        # sorting n * lg n
        a = sorted(a, key=lambda x: (x.x, x.y))
        b = sorted(b, key=lambda x: (x.x, x.y))

        i = 0
        j = 0
        res = []
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                res.append(a[i])
                i += 1
                j += 1
            elif a[i].x == b[j].x:
                if a[i].y > b[j].y:
                    j += 1
                else:
                    i += 1
            elif a[i].x > b[j].x:
                j += 1
            else:
                i += 1
        return res