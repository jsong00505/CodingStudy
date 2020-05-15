from typing import List


class DutchNationalFlag:
    def __init__(self, n: List[str]):
        self.n = n  # buckets

    def swap(self, i: int, j: int):
        temp = self.n[i]
        self.n[i] = self.n[j]
        self.n[j] = temp

    def color(self, i: int) -> str:
        return self.n[i]

    def sort(self):
        colorCall = 0
        swapCall = 0
        n = self.n
        red = 0
        blue = len(n) - 1
        print("before: " + str(self.n))
        if n:
            i = 0
            while i < blue:
                c = self.color(i)
                colorCall += 1
                if c == 'R':
                    if red != i:
                        self.swap(i, red)
                    red += 1
                    i += 1
                elif c == 'B':
                    if i < blue and blue < len(n):
                        self.swap(i, blue)
                        swapCall += 1
                    blue -= 1
                else:
                    i += 1

        print("after: " + str(self.n))
        print("color(): %d, swap() %d" % (colorCall, swapCall))

    def get_bucket(self):
        return self.n
