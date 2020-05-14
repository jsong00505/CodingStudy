from coursera.algorithms.part1.week2.stacks_and_queues.randomized_queue import RandomizedQueue


class Permutation:
    def __init__(self, k, s):
        self.k = k
        self.s = s.split()

    def permutation(self):
        queue = RandomizedQueue()
        for i in self.s:
            queue.enqueue(i)

        it = queue.iterator()

        for i in range(self.k):
            print(it.next())
