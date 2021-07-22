class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort()
        result = [intervals[0]]
        ending_index = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= ending_index:
                result[len(result)-1][1] = max(intervals[i][1], result[len(result)-1][1])
            else:
                result.append(intervals[i])
            ending_index = result[len(result)-1][1]
        return result