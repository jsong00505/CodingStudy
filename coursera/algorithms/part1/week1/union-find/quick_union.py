class quick_union:
    id = []

    def __init__(self, N):
        self.N = N
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


qf = quick_union(10)
print(qf.id)
qf.union(1, 2)
qf.union(1, 3)
print(qf.connected(2, 3))
print(qf.connected(0, 3))
