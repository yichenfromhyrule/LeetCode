class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        # 1. Create a matrix
        matrix = [[0 for a in range(n)] for b in range(m)]
        # 2. Set the first row and col to 1
        for i in range(0, n):
            matrix[0][i] = 1
        for j in range(0, m):
            matrix[j][0] = 1
        # 3. Compute other grid's paths
        for p in range(1, m):
            for q in range(1, n):
                matrix[p][q] = matrix[p-1][q] + matrix[p][q-1]
        return matrix[m-1][n-1]