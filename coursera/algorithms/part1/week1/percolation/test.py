import random

from coursera.algorithms.part1.week1.percolation.percolation import Percolation


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


test_percolation()
