class SelectionSort:
    def sort(self, l):
        for i in range(len(l)):
            min = i
            for j in range(i + 1, len(l)):
                # less
                if l[min] > l[j]:
                    min = j
            # swap
            temp = l[min]
            l[min] = l[j]
            l[j] = temp
        return l

