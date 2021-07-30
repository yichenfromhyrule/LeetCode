import copy


class Solution(object):
    def updateMatrix(self, mat):
        """
        :type mat: List[List[int]]
        :rtype: List[List[int]]
        """
        return self.helperFunction(mat, 0)

    def helperFunction(self, mat, check):
        change = False
        copy_mat = copy.deepcopy(mat)
        for m in range(len(mat)):
            for n in range(len(mat[0])):
                if mat[m][n] > check:
                    surrounding_num = 0
                    surrounding_sum = 0
                    if m - 1 >= 0:
                        surrounding_num += 1
                        surrounding_sum += mat[m - 1][n]
                    if m + 1 < len(mat):
                        surrounding_num += 1
                        surrounding_sum += mat[m + 1][n]
                    if n - 1 >= 0:
                        surrounding_num += 1
                        surrounding_sum += mat[m][n - 1]
                    if n + 1 < len(mat[0]):
                        surrounding_num += 1
                        surrounding_sum += mat[m][n + 1]
                    if surrounding_sum / surrounding_num == mat[m][n]:
                        copy_mat[m][n] += 1
                        change = True
        if change:
            check += 1
            return self.helperFunction(copy_mat, check)
        else:
            return copy_mat