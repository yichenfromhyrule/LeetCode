class Solution(object):
    def diagonalSum(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        r = 0
        n = len(mat)
        for i in range(n):
            if i != (n - i - 1):
                r += (mat[i][i] + mat[i][n - i - 1])
            else:
                r += mat[i][i]
        return r
