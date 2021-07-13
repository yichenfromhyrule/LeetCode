# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def preorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        result = []
        self.preorderTraversalList(root, result)
        return result
    def preorderTraversalList(self, root, result):
        if root:
            result.append(root.val)
            self.preorderTraversalList(root.left, result)
            self.preorderTraversalList(root.right, result)