import random


class KnuthShuffle:
    def shuffle(self, l):
        for i in range(len(l)):
            r = random.randint(0, i)
            temp = l[r]
            l[r] = l[i]
            l[i] = temp