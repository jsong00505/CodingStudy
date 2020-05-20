import unittest

from coursera.algorithms.part1.week3.mergesort.shuffling_linked_list import ShufflingLinkedList, LinkedList


class MyTestCase(unittest.TestCase):
    def test_something(self):
        sll = ShufflingLinkedList()
        node = sll.shuffle(self.gen_linked_list(10))
        print(node)

    def gen_linked_list(self, n: int):
        head = LinkedList(0)
        node = head
        for i in range(1, n):
            node.next = LinkedList(i)
            node = node.next
        return head


if __name__ == '__main__':
    unittest.main()
