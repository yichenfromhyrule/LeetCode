class Solution(object):
    def numSpecial(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: int
        """
        col = []
        for row in mat:
            if sum(row) == 1:
                one_index = row.index(1)
                col.append(one_index)
        r = 0
        for c in col:
            this_col = [mat[i][c] for i in range(len(mat))]
            if sum(this_col)==1:
                r+=1
        return r