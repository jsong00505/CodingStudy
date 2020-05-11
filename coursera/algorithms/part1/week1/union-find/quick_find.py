class QuickFind:
    id = []

    def __init__(self, N):
        self.N = N
        for i in range(N):
            self.id.append(i)

    def connected(self, p, q):
        return self.id[p] == self.id[q]

    def union(self, p, q):
        id = self.id
        pid = id[p]
        qid = id[q]

        # expensive
        for i, v in enumerate(id):
            if i == pid:
                id[i] = qid


qf = QuickFind(10)
print(qf.id)
qf.union(1, 2)
qf.union(1, 3)

assert qf.connected(2, 3) == True
assert qf.connected(0, 3) == False