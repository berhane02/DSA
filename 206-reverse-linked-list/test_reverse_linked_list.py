import pytest
from reverse_linked_list import Solution, ListNode

def list_to_linked_list(nums):
    """Helper function to create a linked list from a list of numbers"""
    if not nums:
        return None
    head = ListNode(nums[0])
    current = head
    for num in nums[1:]:
        current.next = ListNode(num)
        current = current.next
    return head

def linked_list_to_list(head):
    """Helper function to convert linked list to list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

class TestReverseList:
    def test_example1(self):
        sol = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == [5, 4, 3, 2, 1]

    def test_example2(self):
        sol = Solution()
        head = list_to_linked_list([1, 2])
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == [2, 1]

    def test_example3(self):
        sol = Solution()
        head = list_to_linked_list([])
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == []

    def test_single_node(self):
        sol = Solution()
        head = ListNode(1)
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == [1]

    def test_two_nodes(self):
        sol = Solution()
        head = list_to_linked_list([1, 2])
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == [2, 1]

    def test_long_list(self):
        sol = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
        result = sol.reverseList(head)
        assert linked_list_to_list(result) == [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]

