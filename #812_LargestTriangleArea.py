class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        max_area = 0.0
        for i in range(0, len(points)):
            for j in range(1, len(points)):
                for k in range(2, len(points)):
                    curr_area = self.area(points[i], points[j], points[k])
                    max_area = max(curr_area, max_area)
        return max_area
    def area(self, a, b, c):
        return abs(a[0]*b[1]+b[0]*c[1]+c[0]*a[1]-(a[0]*c[1]+c[0]*b[1]+b[0]*a[1])) * 0.5