# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def helperFunction(self, l1, l2, addOne):
        if l1 and l2:
            l1.val = l1.val + l2.val
            l1.val = (l1.val + 1) if addOne else l1.val
            addOne = False
            if l1.val >= 10:
                addOne = True
                l1.val -= 10
            l1.next = self.helperFunction(l1.next, l2.next, addOne)
            return l1
        else:
            l3 = l1 if l1 else l2
            if addOne:
                l3 = self.helperFunction(l3, ListNode(1), False)
            return l3

    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        addOne = False
        result = self.helperFunction(l1, l2, addOne)
        return result


