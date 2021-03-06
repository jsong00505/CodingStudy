class QuickUnion:

    def __init__(self, N):
        self.N = N
        self.id = []
        for i in range(N):
            self.id.append(i)

    def root(self, i):
        # expensive if tree is too tall
        while i != self.id[i]:
            i = self.id[i]
        return i

    def connected(self, p, q):
        return self.root(p) == self.root(q)

    def union(self, p, q):
        i = self.root(p)
        j = self.root(q)
        self.id[i] = j
