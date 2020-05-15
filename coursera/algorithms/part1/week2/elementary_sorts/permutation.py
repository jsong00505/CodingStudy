from typing import List


class Permutation:
    def permutation(self, a: List[int], b: List[int]):
        if all(e in a for e in b):
            return True
        if all(e in b for e in e):
            return True
        return False