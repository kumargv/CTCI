import unittest

def DeleteMiddleNode(node):
    node.data = node.next.data
    node.next = node.next.next

class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

class Test(unittest.TestCase):
    def test_DeleteMiddleNode(self):
        head=Node(1,Node(2, Node(3, Node(4))))
        print(head, head.data, head.next.data, head.next.next.data, head.next.next.next.data)
        DeleteMiddleNode(head.next.next)
        print(head.data)
        self.assertEqual(head.data, 1)
        print(head.next.data)
        self.assertEqual(head.next.data, 2)
        print(head.next.next.data)
        self.assertEqual(head.next.next.data, 4)

if __name__ == "__main__":
  unittest.main()