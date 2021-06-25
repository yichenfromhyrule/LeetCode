# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def hasCycle(self, head):
        """
        :type head: ListNode
        :rtype: bool
        """
        if head == None:
            return False
        elif head.next == None:
            return False
        else:
            slow = head
            fast = head
            if fast.next.next == None:
                return False
            while slow.next != None and fast.next != None and fast.next.next != None:
                slow = slow.next
                fast = fast.next.next
                if slow == fast:
                    return True
            return False
