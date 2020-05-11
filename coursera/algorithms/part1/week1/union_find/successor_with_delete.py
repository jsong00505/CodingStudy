class SuccessorWithDelete:
    id = []
    sz = []
    high = []

    def __init__(self, N):
        self.N = N
        for i in range(N):
            self.id.append(i)
            self.sz.append(1)
            self.high.append(i)

    def root(self, i):
        id = self.id
        # expensive if tree is too tall
        while i != id[i]:
            # path compression
            id[i] = id[id[i]]
            i = id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)

        if i == j:
            return

        # give weight
        if self.sz[i] > self.sz[j]:
            temp = i
            i = j
            j = temp
        self.id[i] = j
        self.sz[j] += self.sz[i]

        high = self.high
        if high[i] > high[j]:
            high[j] = high[i]
        else:
            high[i] = high[j]

    def remove(self, x):
        if x > 0:
            self.union(x, x - 1)

    def successor(self, x):
        return self.high[self.root(x)] + 1
