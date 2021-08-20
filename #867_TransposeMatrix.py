class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        m = len(matrix)
        n = len(matrix[0])
        for i in range(n):
            row = []
            for j in range(m):
                row.append(matrix[j][i])
            result.append(row)
        return result