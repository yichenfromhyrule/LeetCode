# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 1. Write a helper function to get each node's directly parent
        hashmap = {}
        self.helperFunction(root, hashmap)
        # 2. Get each target's ancestor list
        p_parents = [p]
        while p in hashmap:
            p = hashmap[p]
            p_parents.append(p)
        q_parents = [q]
        while q in hashmap:
            q = hashmap[q]
            q_parents.append(q)
        # 4. Find the min same value in two lists
        hashmap_p = {}
        for p_tree in p_parents:
            hashmap_p[p_tree.val] = True
        for q_tree in q_parents:
            if q_tree.val in hashmap_p:
                return q_tree

    def helperFunction(self, root, hashmap):
        if root:
            if root.right:
                hashmap[root.right] = root
            if root.left:
                hashmap[root.left] = root
            self.helperFunction(root.left, hashmap)
            self.helperFunction(root.right, hashmap)

