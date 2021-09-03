class Solution(object):
    def allCellsDistOrder(self, rows, cols, rCenter, cCenter):
        """
        :type rows: int
        :type cols: int
        :type rCenter: int
        :type cCenter: int
        :rtype: List[List[int]]
        """
        count = [[0 for i in range(cols)] for j in range(rows)]
        count[rCenter][cCenter] = 1
        output = [[rCenter, cCenter]]
        stack = [[rCenter, cCenter]]
        while len(stack) > 0:
            check = stack.pop(0)
            r = check[0]
            c = check[1]
            if r - 1 >= 0:
                if count[r-1][c] == 0:
                    output.append([r-1, c])
                    stack.append([r-1, c])
                    count[r-1][c] = 1
            if r + 1 < rows:
                if count[r+1][c] == 0:
                    output.append([r+1, c])
                    stack.append([r+1, c])
                    count[r+1][c] = 1
            if c - 1 >= 0:
                if count[r][c-1] == 0:
                    output.append([r, c-1])
                    stack.append([r, c-1])
                    count[r][c-1] = 1
            if c + 1 < cols:
                if count[r][c+1] == 0:
                    output.append([r, c+1])
                    stack.append([r, c+1])
                    count[r][c+1] = 1
        return output