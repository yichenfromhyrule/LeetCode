class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        r = ""
        num_v = numRows * 2 - 2
        if len(s) <= numRows or numRows == 1:
            return s
        else:
            for row in range(numRows):
                if row == 0:
                    i = 0
                    while i < len(s):
                        r += s[i]
                        i += num_v
                elif row > 0 and row < (numRows - 1):
                    i1 = row
                    while i1 < len(s):
                        i2 = i1 + num_v - row * 2
                        r += s[i1]
                        if i2 < len(s):
                            r += s[i2]
                        i1 += num_v
                elif row == numRows - 1:
                    i = numRows - 1
                    while i < len(s):
                        r += s[i]
                        i += num_v
        return r


if __name__ == '__main__':
    solution = Solution()
    s = "AB"
    numRows = 1
    r= solution.convert(s, numRows)
    print(r)