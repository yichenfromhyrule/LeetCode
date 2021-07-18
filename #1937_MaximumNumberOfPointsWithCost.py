class Solution(object):
    def maxPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        m = len(points)
        n = len(points[0])
        if m == 1:
            return max(points[0])
        for i in range(1, m):
            for j in range(0, n):
                points[i][j] = self.helperFunction(points, i, j)
        return max(points[m-1])

    def helperFunction(self, points, i, j):
        max_value = -1
        prev_list = points[i-1]
        for m in range (0, len(prev_list)):
            curr_value = prev_list[m] + points[i][j] - abs(m-j)
            max_value = curr_value if max_value < curr_value else max_value
        return max_value

if __name__ == '__main__':
    s = Solution()
    points = [[1,5],[2,3],[4,2]]
    r= s.maxPoints(points)
    print(r)