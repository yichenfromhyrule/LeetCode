class Solution(object):
    def floodFill(self, image, sr, sc, newColor):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type newColor: int
        :rtype: List[List[int]]
        """
        m = len(image[0])
        n = len(image)
        result = copy.deepcopy(image)
        color = image[sr][sc]
        check_list = [[sr,sc]]
        while len(check_list) > 0:
            check_gird = check_list.pop(0)
            r = check_gird[0]
            c = check_gird[1]
            if image[r][c] == color:
                result[r][c] = newColor
                if r - 1 >= 0 and result[r-1][c] != newColor:
                    check_list.append([r-1, c])
                if r + 1 < n and result[r+1][c] != newColor:
                    check_list.append([r+1, c])
                if c - 1 >= 0 and result[r][c-1] != newColor:
                    check_list.append([r, c-1])
                if c + 1 < m and result[r][c+1] != newColor:
                    check_list.append([r, c+1])
        return result