# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        copy = result = ListNode(0)
        while head != None:
            if head.val != val:
                copy.next = ListNode(head.val)
                copy = copy.next
            head = head.next
        return result.next
