import pytest
from linked_list_cycle import Solution, ListNode

def create_cycle_list(values, cycle_pos):
    """Helper to create linked list with cycle"""
    if not values:
        return None
    
    nodes = [ListNode(val) for val in values]
    for i in range(len(nodes) - 1):
        nodes[i].next = nodes[i + 1]
    
    if cycle_pos >= 0:
        nodes[-1].next = nodes[cycle_pos]
    
    return nodes[0] if nodes else None

class TestHasCycle:
    def test_example1(self):
        sol = Solution()
        head = create_cycle_list([3, 2, 0, -4], 1)
        assert sol.hasCycle(head) == True

    def test_example2(self):
        sol = Solution()
        head = create_cycle_list([1, 2], 0)
        assert sol.hasCycle(head) == True

    def test_example3(self):
        sol = Solution()
        head = create_cycle_list([1], -1)
        assert sol.hasCycle(head) == False

    def test_no_cycle(self):
        sol = Solution()
        head = ListNode(1)
        head.next = ListNode(2)
        head.next.next = ListNode(3)
        assert sol.hasCycle(head) == False

    def test_single_node_no_cycle(self):
        sol = Solution()
        head = ListNode(1)
        assert sol.hasCycle(head) == False

    def test_empty_list(self):
        sol = Solution()
        head = None
        assert sol.hasCycle(head) == False

    def test_self_cycle(self):
        sol = Solution()
        head = ListNode(1)
        head.next = head
        assert sol.hasCycle(head) == True

