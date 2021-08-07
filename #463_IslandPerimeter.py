class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                result += self.helperFunction(grid, i, j) if grid[i][j] == 1 else 0
        return result

    def helperFunction(self, grid, i, j):
        count = 0
        if i - 1 >= 0:
            count += 1 if grid[i - 1][j] == 1 else 0
        if i + 1 < len(grid):
            count += 1 if grid[i + 1][j] == 1 else 0
        if j - 1 >= 0:
            count += 1 if grid[i][j - 1] == 1 else 0
        if j + 1 < len(grid[0]):
            count += 1 if grid[i][j + 1] == 1 else 0
        return (4 - count)

