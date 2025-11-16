import pytest
from merge_two_sorted_lists import Solution, ListNode

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

class TestMergeTwoLists:
    def test_example1(self):
        sol = Solution()
        list1 = list_to_linked_list([1, 2, 4])
        list2 = list_to_linked_list([1, 3, 4])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [1, 1, 2, 3, 4, 4]

    def test_example2(self):
        sol = Solution()
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == []

    def test_example3(self):
        sol = Solution()
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([0])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [0]

    def test_first_list_empty(self):
        sol = Solution()
        list1 = list_to_linked_list([])
        list2 = list_to_linked_list([1, 2, 3])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [1, 2, 3]

    def test_second_list_empty(self):
        sol = Solution()
        list1 = list_to_linked_list([1, 2, 3])
        list2 = list_to_linked_list([])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [1, 2, 3]

    def test_single_elements(self):
        sol = Solution()
        list1 = list_to_linked_list([1])
        list2 = list_to_linked_list([2])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [1, 2]

    def test_different_lengths(self):
        sol = Solution()
        list1 = list_to_linked_list([1, 3, 5, 7])
        list2 = list_to_linked_list([2, 4])
        result = sol.mergeTwoLists(list1, list2)
        assert linked_list_to_list(result) == [1, 2, 3, 4, 5, 7]

