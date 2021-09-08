class Solution(object):
    def minTimeToVisitAllPoints(self, points):
        """
        :type points: List[List[int]]
        :rtype: int
        """
        result = 0
        for i in range(1, len(points)):
            result += self.helperFunction(points[i-1], points[i])
        return result
    def helperFunction(self, p1, p2):
        if p1[0]==p2[0]:
            return abs(p1[1]-p2[1])
        elif p1[1]==p2[1]:
            return abs(p1[0]-p2[0])
        else:
            abs1 = abs(p1[0]-p2[0])
            abs2 = abs(p1[1]-p2[1])
            return max(abs1, abs2)