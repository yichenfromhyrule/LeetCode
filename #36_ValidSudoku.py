class Solution(object):
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        # 1. Check Row
        for row in board:
            numrow = []
            for num in row:
                if num != ".":
                    numrow.append(num)
            if len(numrow) != len(set(numrow)):
                return False
        # 2. Check Col
        for i in range(9):
            numcol = []
            for row1 in board:
                if row1[i] != ".":
                    numcol.append(row1[i])
            if len(numcol) != len(set(numcol)):
                return False
        # 3. Check subSquare
        for m in range(3):
            for n in range(3):
                numsub = []
                for m1 in range(m*3, m*3+3):
                    for n1 in range(n*3, n*3+3):
                        if board[m1][n1] != ".":
                            numsub.append(board[m1][n1])
                if len(numsub) != len(set(numsub)):
                    return False
        return True