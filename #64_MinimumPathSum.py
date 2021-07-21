class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        # 1. Create a result grid
        m = len(grid)
        n = len(grid[0])
        result = [[0 for a in range(n)] for b in range(m)]
        result[0][0] = grid[0][0]
        # 2. Set the first row and the last row
        for p in range(1, m):
            result[p][0] = result[p - 1][0] + grid[p][0]
        for q in range(1, n):
            result[0][q] = result[0][q - 1] + grid[0][q]
        # 3. Set the rest grid
        for i in range(1, m):
            for j in range(1, n):
                result[i][j] = min(result[i - 1][j], result[i][j - 1]) + grid[i][j]

        return result[m - 1][n - 1]
