import pytest
from binary_tree_level_order_traversal import Solution, TreeNode

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

class TestLevelOrder:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([3, 9, 20, None, None, 15, 7])
        result = sol.levelOrder(root)
        assert result == [[3], [9, 20], [15, 7]]

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([1])
        result = sol.levelOrder(root)
        assert result == [[1]]

    def test_example3(self):
        sol = Solution()
        root = None
        result = sol.levelOrder(root)
        assert result == []

    def test_single_level(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        result = sol.levelOrder(root)
        assert result == [[1], [2, 3]]

    def test_unbalanced_tree(self):
        sol = Solution()
        root = list_to_tree([1, 2, None, 3])
        result = sol.levelOrder(root)
        assert result == [[1], [2], [3]]

    def test_complete_tree(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7])
        result = sol.levelOrder(root)
        assert result == [[1], [2, 3], [4, 5, 6, 7]]

