import unittest
from solution import Solution, ListNode   

def list_to_linkedlist(nums):
    """Helper: convert Python list -> LinkedList"""
    dummy = ListNode(0)
    curr = dummy
    for n in nums:
        curr.next = ListNode(n)
        curr = curr.next
    return dummy.next


def linkedlist_to_list(node):
    """Helper: convert LinkedList -> Python list"""
    result = []
    while node:
        result.append(node.val)
        node = node.next
    return result


class TestAddTwoNumbers(unittest.TestCase):

    def setUp(self):
        self.obj = Solution()

    def test_simple_case(self):
        l1 = list_to_linkedlist([2, 4, 3])   # 342
        l2 = list_to_linkedlist([5, 6, 4])   # 465
        result = self.obj.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), [7, 0, 8])  # 807

    def test_with_carry_over(self):
        l1 = list_to_linkedlist([9, 9, 9])   # 999
        l2 = list_to_linkedlist([1])         # 1
        result = self.obj.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), [0, 0, 0, 1])  # 1000

    def test_different_lengths(self):
        l1 = list_to_linkedlist([2, 4])   # 42
        l2 = list_to_linkedlist([5, 6, 4])   # 465
        result = self.obj.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), [7, 0, 5])  # 507

    def test_both_empty(self):
        l1 = None
        l2 = None
        result = self.obj.addTwoNumbers(l1, l2)
        self.assertEqual(linkedlist_to_list(result), [])


if __name__ == "__main__":
    unittest.main()
