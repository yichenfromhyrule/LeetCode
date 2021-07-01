# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getHeight(self, root):
        return 1 + max(self.getHeight(root.right), self.getHeight(root.left)) if root else 0

    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root:
            if abs(self.getHeight(root.left) - self.getHeight(root.right)) > 1:
                return False
            else:
                return self.isBalanced(root.left) and self.isBalanced(root.right)
        else:
            return True