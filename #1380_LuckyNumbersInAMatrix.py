class Solution(object):
    def luckyNumbers(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        m = len(matrix)
        n = len(matrix[0])
        hashmap = {}
        result = []
        for k in range(m):
            min_row = min(matrix[k])
            hashmap[min_row] = matrix[k].index(min_row)
        for key in hashmap.keys():
            col = [matrix[i][hashmap[key]] for i in range(m)]
            if max(col) == key:
                result.append(key)
        return result