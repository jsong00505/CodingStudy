class WeightedQuickUnion:
    id = []
    sz = []

    def __init__(self, N):
        self.N = N
        for i in range(N):
            self.id.append(i)
            self.sz.append(1)

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
        # give weight
        if self.sz[i] > self.sz[j]:
            temp = i
            i = j
            j = temp
        self.id[i] = j
        self.sz[j] += self.sz[i]


wqu = WeightedQuickUnion(10)
print(wqu.id)
wqu.union(1, 2)
wqu.union(1, 3)
wqu.union(4, 6)
wqu.union(4, 7)
wqu.union(0, 2)

assert wqu.connected(2, 3) == True
assert wqu.connected(1, 7) == False
