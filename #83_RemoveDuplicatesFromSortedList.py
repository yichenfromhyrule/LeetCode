# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helperFunction(self, head):
        if head != None:
            if head.next != None:
                if head.next.val == head.val:
                    head.next = head.next.next
                    self.helperFunction(head)
                else:
                    self.helperFunction(head.next)

    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        self.helperFunction(head)
        return head

