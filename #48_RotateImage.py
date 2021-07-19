class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: None Do not return anything, modify matrix in-place instead.
        """
        result = [[0 for m in range(len(matrix))] for n in range(len(matrix))]

        for i in range(len(matrix)):
            for j in range(len(matrix)):
                result[i][j] = matrix[len(matrix) - j - 1][i]

        for p in range(len(matrix)):
            for q in range(len(matrix)):
                matrix[p][q] = result[p][q]
