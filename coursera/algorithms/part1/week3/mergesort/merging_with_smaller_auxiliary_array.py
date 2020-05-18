from typing import List


class MergingWithSmallerAuxiliaryArray:
    def sort(self, a: List[int], n: int):
        if len(a) != 2 * n:
            ValueError

        auxiliary = a[0: n]

        left = 0
        right = n
        curr = 0
        while left < n or right < 2 * n:
            if left >= n:
                a[curr] = a[right]
                right += 1
            elif right >= 2 * n:
                a[curr] = auxiliary[left]
                left += 1
            elif auxiliary[left] > a[right]:
                a[curr] = a[right]
                right += 1
            else:
                a[curr] = auxiliary[left]
                left =+ 1
            curr += 1
        return a

