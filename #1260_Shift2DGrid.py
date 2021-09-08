class Solution(object):
    def shiftGrid(self, grid, k):
        """
        :type grid: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        grid_list = []
        m = len(grid)
        n = len(grid[0])
        k = k % (m*n)
        for row in grid:
            grid_list += row
        new_list = grid_list[-k:] + grid_list[:(m*n - k)]
        result = []
        result = [new_list[i*n:(i*n)+n] for i in range(0, m)]
        return result