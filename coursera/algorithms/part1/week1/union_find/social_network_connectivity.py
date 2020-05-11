class SocialNetworkConnectivity:
    id = []
    sz = []
    time = 0;

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

    def union(self, p, q, time):
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

        # track the earliest time at which all members are connected(assum time is sorted)
        if self.sz[j] <= len(self.sz):
            self.time = time
