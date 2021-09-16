class Solution(object):
    def busyStudent(self, startTime, endTime, queryTime):
        """
        :type startTime: List[int]
        :type endTime: List[int]
        :type queryTime: int
        :rtype: int
        """
        result = 0
        for s, e in zip(startTime, endTime):
            if s <= queryTime and e >= queryTime:
                result += 1
        return result