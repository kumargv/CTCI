import unittest

def Partition(head, p):
    a_head, a_tail = None, None
    b_head, b_tail = None, None
    node = head
    while node:
        if node.data < p:
            if a_head:
                a_tail.next, a_tail = node, node
            else:
                a_head, a_tail = node, node
        else:
            if b_head:
                b_tail.next, b_tail = node, node
            else:
                b_head, b_tail = node, node
        
        node=node.next
    a_tail.next = b_head
    return a_head

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string+=','+str(self.next)
        return string

class Test(unittest.TestCase):
  def test_partition(self):
    head1 = Node(7,Node(2,Node(9,Node(1,Node(6,Node(3,Node(8)))))))
    head2 = Partition(head1, 6)
    print(head2)
    self.assertEqual(str(head2), "2,1,3,7,9,6,8")
    head3 = Partition(head2, 7)
    print(head3)
    self.assertEqual(str(head3), "2,1,3,6,7,9,8")

if __name__ == "__main__":
  unittest.main()
