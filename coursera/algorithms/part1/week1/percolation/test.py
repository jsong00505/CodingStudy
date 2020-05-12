import random

from coursera.algorithms.part1.week1.percolation.percolation import Percolation
from coursera.algorithms.part1.week1.percolation.percolation_stats import PercolationStats


def test_percolation():
    n = random.randint(3, 10)
    print("n: %d" % n)
    sites = Percolation(n)
    sites.open(1, 1)
    sites.open(1, 2)
    print("is full? " + str(sites.is_full(1, 2)))
    print("percolates? " + str(sites.percolates()))
    sites.open(2, 2)
    print("is full? " + str(sites.is_full(2, 2)))
    print("percolates? " + str(sites.percolates()))
    sites.open(3, 2)
    print("is full? " + str(sites.is_full(3, 2)))
    print("percolates? " + str(sites.percolates()))

def test_percolation_stats_1(n: int, trials: int):
    ps = PercolationStats(n, trials)
    print("mean\t\t\t\t\t = %f" % ps.mean())
    print("stddev\t\t\t\t\t = %f" % ps.stddev())
    print("95% confidence interval\t = " +str(ps.confidence_lo()) + " " +str(ps.confidence_hi()))



#est_percolation()
test_percolation_stats_1(20, 100)
test_percolation_stats_1(20, 100)
test_percolation_stats_1(2, 10000)
test_percolation_stats_1(2, 100000)
