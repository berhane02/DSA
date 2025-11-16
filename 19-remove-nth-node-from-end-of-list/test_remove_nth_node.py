import pytest
from remove_nth_node_from_end_of_list import Solution, ListNode

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

class TestRemoveNthFromEnd:
    def test_example1(self):
        sol = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = sol.removeNthFromEnd(head, 2)
        assert linked_list_to_list(result) == [1, 2, 3, 5]

    def test_example2(self):
        sol = Solution()
        head = list_to_linked_list([1])
        result = sol.removeNthFromEnd(head, 1)
        assert linked_list_to_list(result) == []

    def test_example3(self):
        sol = Solution()
        head = list_to_linked_list([1, 2])
        result = sol.removeNthFromEnd(head, 1)
        assert linked_list_to_list(result) == [1]

    def test_remove_head(self):
        sol = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = sol.removeNthFromEnd(head, 5)
        assert linked_list_to_list(result) == [2, 3, 4, 5]

    def test_remove_tail(self):
        sol = Solution()
        head = list_to_linked_list([1, 2, 3, 4, 5])
        result = sol.removeNthFromEnd(head, 1)
        assert linked_list_to_list(result) == [1, 2, 3, 4]

    def test_single_node(self):
        sol = Solution()
        head = list_to_linked_list([1])
        result = sol.removeNthFromEnd(head, 1)
        assert result is None or linked_list_to_list(result) == []

