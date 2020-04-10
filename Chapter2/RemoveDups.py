import unittest
from LinkedList import LinkedList

def RemoveDups(head):
    nodes = {}
    node = head
    while(node!=None):
        if node.data in node.keys():
            node.data = node.next.data
            node.next = node.next.data
        else:
            nodes[node.data]=1
            node = node.next
            
    return head

def RemoveDups_Second(ll):
    if ll.head is None:
        return

    current = ll.head
    while current:
        runner=current
        while runner.next:
            if runner.next.value == current.value:
                runner.next = runner.next.value
            else:
                runner=runner.next
        current=current.next
    return ll.head

'''
ll = LinkedList()
ll.generate(100, 0, 9)
print (ll)
RemoveDups_Second(ll)
print (ll)
'''
class Node():
    def __init__(self, data, next):
        self.data = data
        self.next = next

class Test(unittest.TestCase):
    def TestRemoveDuplicate(self):
        head = Node(1, Node(3, Node(3, Node(1, Node(5, None)))))
        RemoveDups_Second(head)
        print (head)
        self.assertEqual(head.data, 1)
        self.assertEqual(head.next.data, 3)
        self.assertEqual(head.next.next.data, 5)
        self.assertEqual(head.next.next.next.data, None)

if __name__ == "__main__":
    unittest.main()