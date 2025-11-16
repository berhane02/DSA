import pytest
from lowest_common_ancestor_of_a_binary_tree import Solution, TreeNode

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

def find_node(root, val):
    """Helper to find node with given value"""
    if not root:
        return None
    if root.val == val:
        return root
    left = find_node(root.left, val)
    if left:
        return left
    return find_node(root.right, val)

class TestLowestCommonAncestor:
    def test_example1(self):
        sol = Solution()
        root = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 1)
        result = sol.lowestCommonAncestor(root, p, q)
        assert result.val == 3

    def test_example2(self):
        sol = Solution()
        root = list_to_tree([3, 5, 1, 6, 2, 0, 8, None, None, 7, 4])
        p = find_node(root, 5)
        q = find_node(root, 4)
        result = sol.lowestCommonAncestor(root, p, q)
        assert result.val == 5

    def test_example3(self):
        sol = Solution()
        root = list_to_tree([1, 2])
        p = find_node(root, 1)
        q = find_node(root, 2)
        result = sol.lowestCommonAncestor(root, p, q)
        assert result.val == 1

    def test_same_node(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        p = find_node(root, 2)
        q = find_node(root, 2)
        result = sol.lowestCommonAncestor(root, p, q)
        assert result.val == 2

    def test_root_is_lca(self):
        sol = Solution()
        root = list_to_tree([1, 2, 3])
        p = find_node(root, 2)
        q = find_node(root, 3)
        result = sol.lowestCommonAncestor(root, p, q)
        assert result.val == 1

