import unittest

def Intersection(head_1,head_2):
    nodes={}
    node = head_1
    while node:
        nodes[node] = True
        node = node.next
    node = head_2
    while node:
        if node in nodes:
            return node
        node = node.next
    return None


class Node():
    def __init__(self, data, next=None):
        self.data = data
        self.next = next

    def __str__(self):
        string = str(self.data)
        if self.next:
            string += ',' + str(self.next)
        return string

class Test(unittest.TestCase):
  def test_intersection(self):
    head1 = Node(10,Node(20,Node(30)))
    head2 = Node(20,Node(30,Node(40)))
    self.assertEqual(Intersection(head1, head2), None)
    node = Node(70,Node(80))
    head3 = Node(50,Node(20,node))
    head4 = Node(60,Node(90,Node(10,node)))
    self.assertEqual(Intersection(head3, head4), node)

if __name__ == "__main__":
  unittest.main()