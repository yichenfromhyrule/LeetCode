class Solution(object):
    def imageSmoother(self, img):
        """
        :type img: List[List[int]]
        :rtype: List[List[int]]
        """
        m = len(img)
        n = len(img[0])
        result = [[0 for p in range(n)] for q in range(m)]

        for i in range(m):
            for j in range(n):
                count = 1
                sum_int = img[i][j]
                if i - 1 >= 0:
                    if j - 1 >= 0:
                        count += 1
                        sum_int += img[i - 1][j - 1]
                    if j + 1 < n:
                        count += 1
                        sum_int += img[i - 1][j + 1]
                    count += 1
                    sum_int += img[i - 1][j]
                if i + 1 < m:
                    if j - 1 >= 0:
                        count += 1
                        sum_int += img[i + 1][j - 1]
                    if j + 1 < n:
                        count += 1
                        sum_int += img[i + 1][j + 1]
                    count += 1
                    sum_int += img[i + 1][j]
                if j - 1 >= 0:
                    count += 1
                    sum_int += img[i][j - 1]
                if j + 1 < n:
                    count += 1
                    sum_int += img[i][j + 1]
                result[i][j] = sum_int // count
        return result