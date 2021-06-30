class Solution(object):
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        r = [[1],[1,1]]
        if numRows<=2:
            return r[:numRows]
        else:
            for i in range(2, numRows):
                pre_list = r[i-1]
                curr_list = [1] + [pre_list[j]+pre_list[j+1] for j in range(0,len(pre_list)-1)] + [1]
                r.append(curr_list)
            return r

if __name__ == '__main__':
    s = Solution()
    numRows = 1
    r = s.generate(numRows)
    print(r)