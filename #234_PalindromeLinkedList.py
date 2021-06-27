# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def isPalindrome(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        val_list = []
        while head != None:
            val_list.append(head.val)
            head = head.next
        return val_list == val_list[::-1]