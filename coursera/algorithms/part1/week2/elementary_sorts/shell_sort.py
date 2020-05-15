class ShellSort:
    def sort(self, a):
        N = len(a)
        h = 1
        while (h < N/3):
            h = 3 * h + 1
        while h >= 1:
            # h-sort the array
            for i in (h, N):
                # insertion sort
                j = i
                while a[j] > a[j-h] and j >= h:
                    temp = a[j]
                    a[j] = a[j-h]
                    a[j-h] = temp
                    j -= h
                # move to next increment
                h = h/3