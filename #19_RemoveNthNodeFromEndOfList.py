# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """
        copy = head
        hashmap = {}
        length = 0
        current_index = 0
        while head != None:
            hashmap[current_index] = head
            current_index += 1
            length += 1
            head = head.next
        right_part = hashmap[length - n + 1] if (length - n + 1) in hashmap else None
        result = left_part = ListNode()
        for i in range(0, length - n):
            left_part.next = ListNode(hashmap[i].val)
            left_part = left_part.next
        left_part.next = right_part
        return result.next
