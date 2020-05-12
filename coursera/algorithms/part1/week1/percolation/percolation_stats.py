import math
import random
import statistics

from coursera.algorithms.part1.week1.percolation.percolation import Percolation


class PercolationStats:

    # perform independent trials on an n-by-n grid
    def __init__(self, n: int, trials: int):
        if n <= 0 or trials <= 0:
            raise ValueError

        self.n = n
        self.trials = trials
        self.fractions = []
        t = trials

        while t > 0:
            p = Percolation(n)
            #print(p.percolates())
            while not p.percolates():
                row = random.randint(1, n)
                col = random.randint(1, n)
                if not p.is_open(row, col):
                    p.open(row, col)

            self.fractions.append(p.get_number_of_open_sites() / (n * n))
            #print(self.fractions)
            #print("%d" % p.get_number_of_open_sites())
            t -= 1



    # sample mean of percolation threshold
    def mean(self) -> float:
        return statistics.mean(self.fractions)

    # sample standard deviation of percolation threshold
    def stddev(self) -> float:
        return statistics.pstdev(self.fractions)

    # low endpoint of 95% confidence interval
    def confidence_lo(self) -> float:
        return self.mean() - 1.96 * math.sqrt(self.stddev()) / math.sqrt(self.trials)

    # high endpoint of 95% confidence interval
    def confidence_hi(self) -> float:
        return self.mean() + 1.96 * math.sqrt(self.stddev()) / math.sqrt(self.trials)

