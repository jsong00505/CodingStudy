from coursera.algorithms.part1.week1.analysis_of_algorithms.binary_search import BinarySearch


class ThreeSum:
    def brute_force(self, a):
        n = len(a)
        ans = 0
        for i in range(n - 2):
            for j in range(i + 1, n - 1):
                for k in range(j + 1, n):
                    if a[i] + a[j] + a[k] == 0:
                        ans += 1
        return ans

    def sorting_based(self, a):
        n = len(a)
        ans = 0
        bs = BinarySearch()

        # complexity: n * lg n
        a = sorted(a)

        for i in range(n - 1):
            for j in range(i + 1, n):
                # complexity: n^2 * lg n
                k = bs.search(a, (-1) * (a[i] + a[j]))
                if k != -1 and k > j:
                    ans += 1
        return ans

    def hasing_based(self, a: [int]):
        n = len(a)
        ans = 0

        # complexity: n
        map = {}
        for i in range(n):
            map[a[i]] = i

        for i in range(n - 1):
            for j in range(i + 1, n):
                # complexity: n * n
                k = map.get((-1) * (a[i] + a[j]), -1)
                if k != -1 and k > j:
                    ans += 1
        return ans
