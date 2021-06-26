# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if head == None:
            return head
        else:
            list = []
            while head != None:
                list.append(head.val)
                head = head.next
            result = ListNode()
            copy_result = result
            while len(list) > 0:
                if len(list) > 1:
                    copy_result.val = list.pop(len(list) - 1)
                    next_Node = ListNode()
                    copy_result.next = next_Node
                    copy_result = copy_result.next
                else:
                    copy_result.val = list.pop(len(list) - 1)
            return result

