# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):

    def getResult(self, root, result):
        if root.left != None:
            self.getResult(root.left, result)
        result.append(root.val)
        if root.right != None:
            self.getResult(root.right, result)

    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if root == []:
            return []
        else:
            result = []
            self.getResult(root, result)
            return result
