from typing import List


class Mergesort:
    def sort(self, a: List[int]) -> List[int]:
        if not a:
            return []
        if len(a) == 1:
            return a

        # sort
        mid = len(a) // 2
        left = self.sort(a[0:mid])
        right = self.sort(a[mid:len(a)])

        print(left)
        print(right)

        # merge
        ans = []
        if left[-1] < right[0]:
            ans.extend(left)
            ans.extend(right)
            return ans

        for i in range(len(a)):
            if not left:
                ans.extend(right)
                break
            elif not right:
                ans.extend(left)
                break
            elif left[0] < right[0]:
                ans.append(left.pop(0))
            else:
                ans.append(right.pop(0))
        return ans
