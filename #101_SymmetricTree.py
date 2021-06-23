# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leftList(self, root, result):
        if root != None:
            if root.left != None:
                self.leftList(root.left, result)
            result.append(root.val)
            if root.left != None and root.right == None:
                result.append("r")
            if root.right != None:
                self.leftList(root.right, result)
            if root.right != None and root.left == None:
                result.append("l")

    def rightList(self, root, result):
        if root != None:
            if root.right != None:
                self.rightList(root.right, result)
            result.append(root.val)
            if root.left != None:
                self.rightList(root.left, result)
            if root.right != None and root.left == None:
                result.append("r")
            if root.left != None and root.right == None:
                result.append("l")

    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        if root == None:
            return True
        else:
            if root.left == None and root.right == None:
                return True
            else:
                if root.left != None and root.right != None and root.left.val == root.right.val:
                    leftNode = root.left
                    rightNode = root.right
                    leftResult = []
                    self.leftList(root.left, leftResult)
                    rightResult = []
                    self.rightList(root.right, rightResult)
                    if leftResult == rightResult:
                        return True
                return False
