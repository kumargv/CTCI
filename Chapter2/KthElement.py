import unittest

def KthElement(ll, k):
    current = ll
    runner = ll
    for _ in range(k):
        if not current:
            current=current.next
    while current:
        current = current.next
        runner = runner.next
    return runner

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

#class Test(unittest.TestCase):
#    def KthElement(self):
#        head = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
#        self.assertEqual(None, KthElement(head, 0));
#        print(KthElement(head, 0))
#        self.assertEqual(7, KthElement(head, 1).data);
#        self.assertEqual(4, KthElement(head, 4).data);
#        self.assertEqual(2, KthElement(head, 6).data);
#        self.assertEqual(1, KthElement(head, 7).data);
#        self.assertEqual(None, KthElement(head, 8));

#if __name__ == "__main__":
#  unittest.main()

ll = Node(1,Node(2,Node(3,Node(4,Node(5,Node(6,Node(7)))))))
#ll.generate(10, 0, 99)
print(ll)
ll_result = KthElement(ll, 3)
print(ll_result)