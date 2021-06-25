class MinStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.val = []

    def push(self, val):
        """
        :type val: int
        :rtype: None
        """
        self.val = [val] + self.val

    def pop(self):
        """
        :rtype: None
        """
        return self.val.pop(0)

    def top(self):
        """
        :rtype: int
        """
        return self.val[0]

    def getMin(self):
        """
        :rtype: int
        """
        return min(self.val)

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()