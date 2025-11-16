import pytest
from invert_binary_tree import Solution, TreeNode

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

def tree_to_list(root):
    """Helper to convert tree to list representation"""
    if not root:
        return []
    
    result = []
    queue = [root]
    
    while queue:
        node = queue.pop(0)
        if node:
            result.append(node.val)
            queue.append(node.left)
            queue.append(node.right)
        else:
            result.append(None)
    
    # Remove trailing None values
    while result and result[-1] is None:
        result.pop()
    
    return result

class TestInvertTree:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([4, 2, 7, 1, 3, 6, 9])
        result = sol.invertTree(root)
        assert tree_to_list(result) == [4, 7, 2, 9, 6, 3, 1]

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([2, 1, 3])
        result = sol.invertTree(root)
        assert tree_to_list(result) == [2, 3, 1]

    def test_example3(self):
        sol = Solution()
        root = None
        result = sol.invertTree(root)
        assert result is None

    def test_single_node(self):
        sol = Solution()
        root = TreeNode(1)
        result = sol.invertTree(root)
        assert result.val == 1
        assert result.left is None
        assert result.right is None

    def test_left_skewed(self):
        sol = Solution()
        root = list_to_tree([1, 2, None, 3])
        result = sol.invertTree(root)
        assert tree_to_list(result) == [1, None, 2, None, None, None, 3]

