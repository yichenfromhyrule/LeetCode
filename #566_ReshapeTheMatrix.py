class Solution(object):
    def matrixReshape(self, mat, r, c):
        """
        :type mat: List[List[int]]
        :type r: int
        :type c: int
        :rtype: List[List[int]]
        """
        mat_line = []
        for row in mat:
            for num in row:
                mat_line.append(num)
        if c*r != len(mat_line):
            return mat
        else:
            result = []
            for i in range(r):
                result.append(mat_line[i*c:(i+1)*c])
            return result