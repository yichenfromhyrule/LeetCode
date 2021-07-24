class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        addOne = False
        result = ""
        while len(num1) > 0 and len(num2) > 0:
            a = num1[-1]
            b = num2[-1]
            num1 = num1[:len(num1) - 1]
            num2 = num2[:len(num2) - 1]
            r = int(a) + int(b)
            if addOne:
                r += 1
                addOne = False
            if r >= 10:
                r -= 10
                addOne = True
            result += str(r)
        num3 = num1 if len(num1) > 0 else num2
        if len(num3) == 0:
            return "1" + result[::-1] if addOne else result[::-1]
        else:
            num3 = int(num3) if not addOne else (int(num3) + 1)
            result = str(num3) + result[::-1]
            return result
