# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        copy = head
        while copy and copy.next:
            copy_val = copy.val
            copy.val = copy.next.val
            copy.next.val = copy_val
            copy = copy.next.next
        else:
            return head