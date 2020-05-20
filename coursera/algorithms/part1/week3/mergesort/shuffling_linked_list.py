import random


class LinkedList(object):
    def __init__(self, val: int):
        self.val = val
        self.next = None

    def __repr__(self):
        res = []
        temp = self
        while temp:
            res.append(temp.val)
            temp = temp.next
        return str(' '.join((str(x) for x in res)))

class ShufflingLinkedList:
    def shuffle(self, head: LinkedList) -> LinkedList:
        result = None
        start = None
        while head.next:
            rand = self.get_random(head)
            if start:
                start.next = rand.next
                start = start.next
            else:
                start = rand.next
                result = start
            if rand.next:
                rand.next = rand.next.next
            if start:
                start.next = None
        start.next = head
        return result

    def get_random(self, head: LinkedList) -> LinkedList:
        fast = head
        slow = head

        while fast and fast.next and fast.next.next and random.randint(0, 4):
            slow = slow.next
            fast = fast.next.next

        return slow
