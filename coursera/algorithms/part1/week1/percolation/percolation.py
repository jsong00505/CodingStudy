from coursera.algorithms.part1.week1.union_find.weighted_quick_union import WeightedQuickUnion


class Percolation:
    # perform independent trials on an n-by-n grid
    def __init__(self, n):
        self.n = n
        self.sites = [[False] * (n + 1) for _ in range(n+1)]
        self.number_of_open_sites = 0
        self.wqu = WeightedQuickUnion(n * n)

    # opens the site (row, col) if it is not open already
    def open(self, row, col):

        if self.is_open(row, col):
            return

        wqu = self.wqu

        if self.is_out_range(row, col):
            raise ValueError
        self.sites[row][col] = True
        #print("open [%d][%d]" % (row, col))
        self.number_of_open_sites += 1

        # up
        if not self.is_out_range(row - 1, col) and self.is_open(row - 1, col):
            wqu.union(self.to_2d(row, col), self.to_2d(row - 1, col))

        # down
        if not self.is_out_range(row + 1, col) and self.is_open(row + 1, col):
            wqu.union(self.to_2d(row, col), self.to_2d(row + 1, col))

        # left
        if not self.is_out_range(row, col - 1) and self.is_open(row, col - 1):
            wqu.union(self.to_2d(row, col), self.to_2d(row, col - 1))

        # right
        if not self.is_out_range(row, col + 1) and self.is_open(row, col + 1):
            wqu.union(self.to_2d(row, col), self.to_2d(row, col + 1))

    # is the site (row, col) open?
    def is_open(self, row, col):
        if self.is_out_range(row, col):
            print("%d %d" %(row, col))
            raise ValueError
        return self.sites[row][col]

    # is the site (row, col) full?
    def is_full(self, row, col):
        if self.is_out_range(row, col):
            raise ValueError
        for i in range(self.n):
            if self.wqu.connected(self.to_2d(row, col), i):
                return True
        return False

    # returns the number of open sites
    def get_number_of_open_sites(self):
        return self.number_of_open_sites;

    # does the system percolate?
    def percolates(self):
        top = 0
        bottom = self.n * (self.n - 1)

        for i in range(top, self.n):
            for j in range(bottom, bottom + self.n):
                if self.wqu.connected(i, j):
                    #print(self.sites)
                    return True
        return False

    def is_out_range(self, row, col):
        return row < 1 or row > self.n or col < 1 or col > self.n

    def to_2d(self, row, col):
        return (row - 1) * self.n + (col - 1)


