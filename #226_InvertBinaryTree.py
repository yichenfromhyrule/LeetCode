# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def invertLeftAndRight(self, root):
        if root != None:
            left_node = None
            right_node = None
            if root.left != None:
                left_node = root.left
            if root.right != None:
                right_node = root.right
            root.left = right_node
            root.right = left_node
            self.invertLeftAndRight(root.right)
            self.invertLeftAndRight(root.left)

    def invertTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        self.invertLeftAndRight(root)
        return root
