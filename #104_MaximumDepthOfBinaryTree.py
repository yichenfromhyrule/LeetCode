# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def findDepth(self, root, depth, record, depth_list):
        depth_list.append(depth)
        while len(record) > 0:
            root = record.pop()
            if root.left != None:
                record.append(root.left)
                self.findDepth(root.left, depth + 1, record, depth_list)
            if root.right != None:
                record.append(root.right)
                self.findDepth(root.right, depth + 1, record, depth_list)

    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            return 0
        else:
            record = [root]
            d = 1
            depth_list = []
            self.findDepth(root, d, record, depth_list)
            return max(depth_list)