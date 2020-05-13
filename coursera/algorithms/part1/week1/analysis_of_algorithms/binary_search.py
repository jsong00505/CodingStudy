class BinarySearch:
    def search(self, l: [int], target: int) -> int:
        hi = len(l) - 1
        lo = 0

        while lo <= hi:
            mid = lo + int((hi - lo) / 2)
            if l[mid] == target:
                return mid
            elif l[mid] > target:
                hi = mid - 1
            else:
                lo = mid + 1
        return -1
