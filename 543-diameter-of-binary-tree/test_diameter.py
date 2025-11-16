import pytest
from diameter_of_binary_tree import Solution, TreeNode

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

class TestDiameterOfBinaryTree:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3, 4, 5])
        assert sol.diameterOfBinaryTree(root) == 3

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([1, 2])
        assert sol.diameterOfBinaryTree(root) == 1

    def test_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        assert sol.diameterOfBinaryTree(root) == 0

    def test_empty_tree(self):
        sol = Solution()
        root = None
        assert sol.diameterOfBinaryTree(root) == 0

    def test_left_skewed(self):
        sol = Solution()
        root = list_to_tree([1, 2, None, 3, None, 4])
        assert sol.diameterOfBinaryTree(root) == 3

    def test_balanced_tree(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3, 4, 5, 6, 7])
        result = sol.diameterOfBinaryTree(root)
        assert result >= 4

