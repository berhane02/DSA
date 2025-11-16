import pytest
from validate_binary_search_tree import Solution, TreeNode

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

class TestIsValidBST:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([2, 1, 3])
        assert sol.isValidBST(root) == True

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([5, 1, 4, None, None, 3, 6])
        assert sol.isValidBST(root) == False

    def test_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        assert sol.isValidBST(root) == True

    def test_invalid_left_subtree(self):
        sol = Solution()
        root = list_to_tree([5, 4, 6, None, None, 3, 7])
        assert sol.isValidBST(root) == False

    def test_valid_tree(self):
        sol = Solution()
        root = list_to_tree([10, 5, 15, None, None, 12, 20])
        assert sol.isValidBST(root) == True

    def test_invalid_right_subtree(self):
        sol = Solution()
        root = list_to_tree([10, 5, 15, None, None, 6, 20])
        assert sol.isValidBST(root) == False

    def test_duplicate_values(self):
        sol = Solution()
        root = list_to_tree([1, 1])
        assert sol.isValidBST(root) == False

