import pytest
from same_tree import Solution, TreeNode

def list_to_tree(nums):
    """Helper to create tree from list representation"""
    if not nums:
        return None
    
    def build_tree(index):
        if index >= len(nums) or nums[index] is None:
            return None
        node = TreeNode(nums[index])
        node.left = build_tree(2 * index + 1)
        node.right = build_tree(2 * index + 2)
        return node
    
    return build_tree(0)

class TestIsSameTree:
    def test_example1(self):
        sol = Solution()
        p = list_to_tree([1, 2, 3])
        q = list_to_tree([1, 2, 3])
        assert sol.isSameTree(p, q) == True

    def test_example2(self):
        sol = Solution()
        p = list_to_tree([1, 2])
        q = list_to_tree([1, None, 2])
        assert sol.isSameTree(p, q) == False

    def test_example3(self):
        sol = Solution()
        p = list_to_tree([1, 2, 1])
        q = list_to_tree([1, 1, 2])
        assert sol.isSameTree(p, q) == False

    def test_both_empty(self):
        sol = Solution()
        p = None
        q = None
        assert sol.isSameTree(p, q) == True

    def test_one_empty(self):
        sol = Solution()
        p = list_to_tree([1])
        q = None
        assert sol.isSameTree(p, q) == False

    def test_single_node_same(self):
        sol = Solution()
        p = TreeNode(1)
        q = TreeNode(1)
        assert sol.isSameTree(p, q) == True

    def test_single_node_different(self):
        sol = Solution()
        p = TreeNode(1)
        q = TreeNode(2)
        assert sol.isSameTree(p, q) == False

    def test_different_structure(self):
        sol = Solution()
        p = list_to_tree([1, 2])
        q = list_to_tree([1, None, 2])
        assert sol.isSameTree(p, q) == False

