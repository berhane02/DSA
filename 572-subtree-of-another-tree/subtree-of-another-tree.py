# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSubtree(self, root, subRoot):
        """
        :type root: Optional[TreeNode]
        :type subRoot: Optional[TreeNode]
        :rtype: bool
        """
       
        if root is None:
            if subRoot is None:
                return True
            else:
                return False
        def helper(curr, subRoot):
            if curr is None and subRoot is None:
                return True
            if curr is None or subRoot is None:
                return False
            return (curr.val == subRoot.val and helper(curr.left, subRoot.left) and helper(curr.right, subRoot.right))
        q = deque([root])
    
        while q:
            curr = q.popleft()
            if curr.val == subRoot.val:
                if helper(curr, subRoot):
                    return True
            if curr.left:
                q.append(curr.left)
            if curr.right:
                q.append(curr.right)
        return False