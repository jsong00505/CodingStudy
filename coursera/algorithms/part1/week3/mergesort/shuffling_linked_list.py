
class LinkedList(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None

class ShufflingLinkedList:
    def shuffle(self, a: LinkedList) -> LinkedList:
        return a