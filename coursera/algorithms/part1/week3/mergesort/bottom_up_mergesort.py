class BottomUpMergesort:
    def sort(self, a):
        size = 1
        res = []
        while size < len(a):
            lo = 0
            while lo <= len(a):
                mid = min(lo + size, len(a))
                hi = min(lo + 2 * size, len(a))
                left = a[lo:mid]
                right = a[mid:hi]
                if not left:
                    res.extend(right)
                elif not right:
                    res.extend(left)
                elif left[-1] < right[0]:
                    res.extend(left)
                    res.extend(right)
                else:
                    while left or right:
                        if not left:
                            res.extend(right)
                            right = []
                        elif not right:
                            res.extend(left)
                            left = []
                        elif left[0] > right[0]:
                            res.append(right.pop(0))
                        else:
                            res.append(left.pop(0))
                lo += size + size
            size += size
            a = res.copy()
            res = []
        return a
