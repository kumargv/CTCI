import unittest

def SumNumbers(number_1, number_2):
    node1 = number_1
    node2 = number_2
    carry = 0
    sum_head, sum_node = None, None
    while node1 or node2 or carry:
        value = carry
        if node1:
            value+= node1.data
            node1 = node1.next
        if node2:
            value+= node2.data
            node2 = node2.next
        if sum_node:
            sum_node.next = Node(value%10)
            sum_node = sum_node.next
        else:
            sum_node = Node(value%10)
            sum_head = sum_node
        carry = value/10
    return sum_head

#def SumNumbers_FollowUp(number_1, number_2):
#    if len(number_1) < len(number_2):
#        for i in range

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
  def test_sum_lists(self):
    num1 = Node(1,Node(2,Node(3)))
    num2 = Node(4,Node(9,Node(5)))
    sum_number = SumNumbers(num1, num2)
    print(sum_number)
    self.assertEqual(str(sum_number), "5,1,9")
    num1 = Node(9,Node(2,Node(3,Node(4,Node(1)))))
    num2 = Node(4,Node(9,Node(8)))
    sum_number = SumNumbers(num1, num2)
    print(sum_number)
    self.assertEqual(str(sum_number), "3,2,2,5,1")

if __name__ == "__main__":
  unittest.main()