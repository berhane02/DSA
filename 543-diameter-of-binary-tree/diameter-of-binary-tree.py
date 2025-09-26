# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def diameterOfBinaryTree(self, root):
        """
        :type root: Optional[TreeNode]
        :rtype: int
        """
        self.diameter = 0
        def dfs(node):
            if not node:
                return 0
            l = dfs(node.left)
            r = dfs (node.right)
            self.diameter = max(self.diameter, l + r)
            return 1+max(l, r)
        dfs(root)
        return self.diameter