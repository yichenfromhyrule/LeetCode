class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        result = []
        for row in image:
            new_row = []
            for grid in row[::-1]:
                new_row.append(1 - grid)
            result.append(new_row)
        return result
