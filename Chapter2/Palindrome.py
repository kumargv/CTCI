import unittest

def Palindrome(head):
    fwd, bwd = head, Copy_Reverse(head)
    while fwd:
        if fwd.data !=bwd.data:
            return False
        fwd, bwd = fwd.next, bwd.next
    return True

def Copy_Reverse(head):
    prev = None
    node = copy(head)
    while node:
        next = node.next
        node.next = prev
        prev = node
        node = copy(next)
    return prev

def copy(node):
    if node:
        return Node(node.data, node.next)
    else:
        return None

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
  def test_palindrome(self):
    list1 = Node(10)
    self.assertTrue(Palindrome(list1))
    list2 = Node(10,Node(10))
    self.assertTrue(Palindrome(list2))
    list3 = Node(10,Node(20))
    self.assertFalse(Palindrome(list3))
    list4 = Node(10,Node(70,Node(30,Node(70,Node(10)))))
    self.assertTrue(Palindrome(list4))

if __name__ == "__main__":
  unittest.main()