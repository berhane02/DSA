import pytest
from add_two_numbers import Solution, ListNode

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

class TestAddTwoNumbers:
    def test_example1(self):
        sol = Solution()
        l1 = list_to_linked_list([2, 4, 3])
        l2 = list_to_linked_list([5, 6, 4])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [7, 0, 8]

    def test_example2(self):
        sol = Solution()
        l1 = list_to_linked_list([0])
        l2 = list_to_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0]

    def test_example3(self):
        sol = Solution()
        l1 = list_to_linked_list([9, 9, 9, 9, 9, 9, 9])
        l2 = list_to_linked_list([9, 9, 9, 9])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [8, 9, 9, 9, 0, 0, 0, 1]

    def test_different_lengths(self):
        sol = Solution()
        l1 = list_to_linked_list([1, 8])
        l2 = list_to_linked_list([0])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [1, 8]

    def test_carry_over(self):
        sol = Solution()
        l1 = list_to_linked_list([5])
        l2 = list_to_linked_list([5])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0, 1]

    def test_single_digit(self):
        sol = Solution()
        l1 = list_to_linked_list([9])
        l2 = list_to_linked_list([1])
        result = sol.addTwoNumbers(l1, l2)
        assert linked_list_to_list(result) == [0, 1]

