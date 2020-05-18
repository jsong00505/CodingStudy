from typing import List

"""
An inversion in an array a[] is a pair of entries a[i] and a[j] such that i < j but a[i] > a[j]. 
Given an array, design a linearithmic algorithm to count the number of inversions.
"""


class CountingInversions:

    def count(self, a: List[int]) -> List[int]:
        # 9 8 7 6 5
        size = 1
        cnt = 0

        while size < len(a):
            lo = 0
            temp = []
            while lo <= len(a):
                mid = min(lo + size, len(a))
                hi = min(lo + 2 * size, len(a))
                left = a[lo:mid]
                right = a[mid:hi]
                while left or right:
                    if not left:
                        temp.append(right.pop(0))
                    elif not right:
                        temp.append(left.pop(0))
                    elif left[0] < right[0]:
                        temp.append(left.pop(0))
                    else:
                        temp.append(right.pop(0))
                        cnt += len(left)
                lo += 2 * size
            a = temp
            size += size
        return cnt
