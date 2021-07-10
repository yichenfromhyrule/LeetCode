class Solution(object):
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """
        r = [[1], [1, 1]]
        if rowIndex <= 1:
            return r[rowIndex]
        else:
            for i in range(2, rowIndex + 1):
                pre_list = r[i - 1]
                curr_list = [1] + [pre_list[j] + pre_list[j + 1] for j in range(0, len(pre_list) - 1)] + [1]
                r.append(curr_list)
            return r[rowIndex]
if __name__ == '__main__':
    s = Solution()
    x = 10
    n = 3
    r = s.divide(x,n)
    print(r)