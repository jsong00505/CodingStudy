class QuickFind:
    def __init__(self, N):
        self.N = N
        self.id = []
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
