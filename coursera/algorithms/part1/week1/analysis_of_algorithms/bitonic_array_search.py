class BitonicArraySearch:
    def search(self, a: [int], target: int) -> int:
        if not self.is_bitonic(a):
            return -1

        point = self.find_bitonic_point(a)

        res = self.search_in_increase(a, point, 0, target)
        if res == -1:
            res = self.search_in_decrease(a, len(a) - 1, point, target)

        return res

    def search_in_increase(self, a: [int], hi: int, lo: int, target: int) -> int:
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == target:
                return mid
            elif a[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1

    def search_in_decrease(self, a: [int], hi: int, lo: int, target: int) -> int:
        while lo <= hi:
            mid = lo + (hi - lo) // 2
            if a[mid] == target:
                return mid
            elif a[mid] > target:
                lo = mid + 1
            else:
                hi = mid - 1
        return -1

    def is_bitonic(self, a):
        n = len(a)
        if n < 3:
            return False

        increased = False
        decreased = False

        for i in range(n - 1):
            if a[i] < a[i + 1]:
                if not decreased:
                    increased = True  # /
                else:
                    return False  # /\/
            elif a[i] == a[i + 1]:
                return False  # /-
            else:
                if increased:
                    decreased = True  # /\
                else:
                    return False  # \

        if decreased:
            return True  # /\
        else:
            return False  # /

    def find_bitonic_point(self, a):
        hi = len(a) - 1
        lo = 0

        while True:
            mid = lo + (hi - lo) // 2
            prev = a[mid - 1]
            point = a[mid]
            next = a[mid + 1]

            if prev < point:
                if point > next:
                    return mid
                else:
                    lo = mid
            else:
                hi = mid
