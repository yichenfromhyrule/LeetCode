class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        character_list = ['Z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
                          'S', 'T', 'U', 'V', 'W', 'X', 'Y']
        r = columnNumber
        result = ""
        while r > 0:
            r, m = self.divideFunction(r)
            result = character_list[m] + result
            if m == 0:
                r -= 1

        return result

    def divideFunction(self, num):
        r = num // 26
        m = num % 26
        return (r, m)