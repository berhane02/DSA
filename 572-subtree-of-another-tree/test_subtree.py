import pytest
from subtree_of_another_tree import Solution, TreeNode

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

class TestIsSubtree:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([3, 4, 5, 1, 2])
        subRoot = list_to_tree([4, 1, 2])
        assert sol.isSubtree(root, subRoot) == True

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([3, 4, 5, 1, 2, None, None, None, None, 0])
        subRoot = list_to_tree([4, 1, 2])
        assert sol.isSubtree(root, subRoot) == False

    def test_same_tree(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        subRoot = list_to_tree([1, 2, 3])
        assert sol.isSubtree(root, subRoot) == True

    def test_subtree_at_root(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        subRoot = list_to_tree([1])
        assert sol.isSubtree(root, subRoot) == False  # Need exact match

    def test_subtree_not_present(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        subRoot = list_to_tree([4, 5, 6])
        assert sol.isSubtree(root, subRoot) == False

    def test_empty_subtree(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        subRoot = None
        assert sol.isSubtree(root, subRoot) == True

    def test_single_node_match(self):
        sol = Solution()
        root = TreeNode(1)
        subRoot = TreeNode(1)
        assert sol.isSubtree(root, subRoot) == True

    def test_single_node_no_match(self):
        sol = Solution()
        root = TreeNode(1)
        subRoot = TreeNode(2)
        assert sol.isSubtree(root, subRoot) == False

