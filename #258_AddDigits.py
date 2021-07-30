class Solution(object):
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num > 9:
            r = 0
            for c in str(num):
                r += int(c)
            num = r
        return num