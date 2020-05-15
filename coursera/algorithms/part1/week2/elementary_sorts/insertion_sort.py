class InsertionSort:
    def sort(self, l):
        for i in range(1, len[l]):
            j = i
            if l[j-1] > l[j]:
                while j > 0 and l[j-1] > l[j]:
                    temp = l[j-1]
                    l[j-1] = l[j]
                    l[j] = temp
                    j -= 1
        return l

